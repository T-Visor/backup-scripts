"""
Source: https://codereview.stackexchange.com/questions/101616

Original Author: magu_ (2015)
Modified By: T-Visor (2020)

Description: This backup script creates the root structure in another
             folder, and syncs everything which recursively lies within each
             source folder. For files bigger than the specified threshold,
             they are first compressed.

format: python3 sync.py -target MY_BACKUPFOLDER -source SRC_1 SRC_2
"""

import argparse
import gzip
import os
import shutil
import sys
import time
from threading import Thread

# flag variable shared between threads
SYNC_THREAD_FINISHED = False




def main():
    """ 
        Run the backup.
    """
    print('******************Syncing files******************')
    arguments = parse_input()
    start = time.time()

    for root in arguments.source:
        sync_thread = Thread(target=sync_root, args=(root, arguments, ))
        sync_thread.start()
        animation_thread = Thread(target=display_waiting_animation, args=())
        animation_thread.start()
        sync_thread.join()
        animation_thread.join()

    end = time.time()
    print('Elapsed time: {} second(s)'.format(end - start))
    print('******************Done***************************')




def parse_input():
    """ 
        Parse the arguments from the command-line.

        - Text after '-target' specifies the target directory
          (path cannot have spaces)
        - Text after '-source' specifies source directory or directories
        - Text after '-compress' specifies zipping threshold with Gzip
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-target', nargs=1, required=True,
                        help='Target Backup folder')
    parser.add_argument('-source', nargs='+', required=True,
                        help='Source Files to be added')
    parser.add_argument('-compress', nargs=1,  type=int,
                        help='Gzip threshold in bytes', default=[9000000000])

    # if no arguments were passed, show the help screen
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    return parser.parse_args()




def sync_root(root, arguments):
    """ 
        Construct the root file structure (root-to-source)
        in the target directory before copying files.

        - root : the root directory (string)
        - arguments : command-line arguments
    """
    target = arguments.target[0]
    compress = arguments.compress[0]

    try:
        for path, _, files in os.walk(root):
            for source in files:
                source = path + '/' + source
                sync_file(source, target + source, compress)
    except PermissionError:
        print('Target directory not found... cannot perform backup.')
    finally:
        global SYNC_THREAD_FINISHED
        SYNC_THREAD_FINISHED = True




def sync_file(source, target, compress):
    """ 
        Determines if any changes were made to the source file
        since the last sync. If so, copy the new file to the target folder.

        - source : source file path (string)
        - target : target file path (string)
        - compress : Gzip threshold in bytes (int)
    """
    size = size_if_newer(source, target)

    if size:
        transfer_file(source, target, size > compress)




def size_if_newer(source, target):
    """ 
        If source is newer return its size, otherwise return False.

        - source : source file path (string)
        - target : target file path (string)
    """
    src_stat = os.stat(source)
    try:
        target_ts = os.stat(target).st_mtime
    except FileNotFoundError:
        try:
            target_ts = os.stat(target + '.gz').st_mtime
        except FileNotFoundError:
            target_ts = 0

    # The time difference of one second is necessary since subsecond accuracy
    # of os.st_mtime is striped by copy2
    return src_stat.st_size if (src_stat.st_mtime - target_ts > 1) else False




def transfer_file(source, target, compress):
    """ 
        Either copy, or compress and copy the file.

        - source : source file path (string)
        - target : target file path (string)
        - compress : Gzip threshold in bytes (int)
    """
    try:
        if compress:
            with gzip.open(target + '.gz', 'wb') as target_fid:
                with open(source, 'rb') as source_fid:
                    target_fid.writelines(source_fid)
        else:
            shutil.copy2(source, target)
    except FileNotFoundError:
        os.makedirs(os.path.dirname(target))
        transfer_file(source, target, compress)




def display_waiting_animation():
    """ 
        Displays an animated progress bar while the sync thread is running.

        Source: https://stackoverflow.com/questions/22029562/

        Original Author: Python Pro
    """
    animation_states = ['[■□□□□□□□□□]', '[■■□□□□□□□□]', '[■■■□□□□□□□]',
                        '[■■■■□□□□□□]', '[■■■■■□□□□□]', '[■■■■■■□□□□]',
                        '[■■■■■■■□□□]', '[■■■■■■■■□□]', '[■■■■■■■■■□]',
                        '[■■■■■■■■■■]', '[□■■■■■■■■■]', '[□□■■■■■■■■]',
                        '[□□□■■■■■■■]', '[□□□□■■■■■■]', '[□□□□□■■■■■]',
                        '[□□□□□□■■■■]', '[□□□□□□□■■■]', '[□□□□□□□□■■]',
                        '[□□□□□□□□□■]', '[□□□□□□□□□□]']

    erase_line = '\x1b[2K'

    i = 0
    while not SYNC_THREAD_FINISHED:
        time.sleep(0.1)
        # carriage return then write an animation state
        sys.stdout.write('\r' + animation_states[i % len(animation_states)])
        sys.stdout.flush()
        i += 1

    # erase the progress bar when it is no longer needed
    sys.stdout.write('\r')
    sys.stdout.write(erase_line)




main()
