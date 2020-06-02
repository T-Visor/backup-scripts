import datetime
import os
import shutil

SOURCE_DIRECTORY = '/home/t-visor/Music'
DESTINATION_DIRECTORY = '/home/t-visor/Downloads'

def main():
    """
        Run one or more backups with code in main.
    """
    print('********STARTING BACKUP********')
    perform_backup(SOURCE_DIRECTORY, DESTINATION_DIRECTORY)
    print('********FINISHED********')

#======================================================================

def create_backup_directory(base_directory):
    """
        Returns a path with the current date
        which will be used to store the contents
        of the backup.

        (Format: Year-Month-Date_HourMinute)

        - dated_directory : the dated path for backup contents
                            (String)
    """
    date = datetime.datetime.now().strftime('%Y-%m-%d_%H%M')
    dated_directory = base_directory + '/' + date
    return dated_directory

def copy_files(src_directory, dest_directory):
    """
        Copy files/folders from source directory to
        destination directory.

        - src_directory : the source directory (String)
        - dest_directory : the destination directory (String)
    """
    shutil.copytree(src_directory, dest_directory)

def perform_backup(src_directory, dest_directory):
    """
        Run the backup by creating a folder with the current
        date and copy the desired source directory's contents
        to the newly created folder.

        - src_directory : the source directory (String)
        - dest_directory : the destination directory (String)
    """
    dated_directory = create_backup_directory(dest_directory)
    print('Creating directory {} for backup'.format(dated_directory))
    copy_files(src_directory, dated_directory)

main()
