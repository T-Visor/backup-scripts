"""
Source: https://codereview.stackexchange.com/questions/101616/simple-backup-script-in-python

Original Author: magu_ (2015)
Modified By: T-Visor (2020)

Description: Simple backup script which just creates the root structure in an other
             folder and syncs everything which recursevely lies within one of the source
             folders. For files bigger than a threshold they are first Gziped.

example use: python3 sync.py -target MY_BACKUPFOLDER -source ARG_1 ARG_2
"""

import argparse
import gzip
import os
import shutil
import sys

def main():
    """ Run the backup script.
    """
    arguments = parse_input()
    print('### Start copy ###')
    for root in arguments.source:
        sync_root(root, arguments)
    print('### Done ###')

#==========================================================================

def parse_input():
    """ Parse the arguments from the command-line.

        - Text before '-target' specifies target directory
          (path cannot have spaces)
        - Text before '-source' specify source(s)
        - Text before '-compress' specifies zipping with Gzip
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-target', nargs=1, required=True,
                        help='Target Backup folder')
    parser.add_argument('-source', nargs='+', required=True,
                        help='Source Files to be added')
    parser.add_argument('-compress', nargs=1,  type=int,
                        help='Gzip threshold in bytes', default=[1000000000])

    # if no arguments were passed, show the help screen 
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    return parser.parse_args()


def size_if_newer(source, target):
    """ If source is newer return its size, otherwise return False.

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


def sync_file(source, target, compress):
    """ Determines if any changes were made to the source file
        since the last sync. If so, copy the new file to the target folder.

        - source : source file path (string)
        - target : target file path (string)
        - compress : Gzip threshold in bytes (int)
    """
    size = size_if_newer(source, target)

    if size:
        transfer_file(source, target, size > compress)


def transfer_file(source, target, compress):
    """ Either copy or compress and copy the file.

        - source : source file path (string)
        - target : target file path (string)
        - compress : Gzip threshold in bytes (int)
    """
    try:
        if compress:
            with gzip.open(target + '.gz', 'wb') as target_fid:
                with open(source, 'rb') as source_fid:
                    target_fid.writelines(source_fid)
            print('Compress {}'.format(source))
        else:
            shutil.copy2(source, target)
            print('Copy {}'.format(source))
    except FileNotFoundError:
        os.makedirs(os.path.dirname(target))
        transfer_file(source, target, compress)


def sync_root(root, arguments):
    """ Construct the proper path in the target directory
        before copying any files.

        - root : the root directory file path (string)
        - arguments : command-line arguments
    """
    target = arguments.target[0]
    compress = arguments.compress[0]

    for path, _, files in os.walk(root):
        for source in files:
            source = path + '/' + source
            sync_file(source, target + source, compress)


main()
