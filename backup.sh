#!/bin/bash

# Backup drive paths
UGREEN_DRIVE="/media/t-visor/ugreen-drive/my-backups/my-files"  
WD_DRIVE="/media/t-visor/wd-drive/my-backups/my-files" 

# Source and target directories for backup
TARGET_DIRECTORY=value
SOURCE_DIRECTORY="/home/t-visor/Documents"

# Console text colors
RED='\033[1;33m'
PURPLE='\033[1;35m'
NO_COLOR='\033[0m'

start_sync () {
    TARGET_DIRECTORY=$1
    echo -e "${RED}SOURCE: $SOURCE_DIRECTORY"
    echo -e "${PURPLE}DESTINATION: $TARGET_DIRECTORY"
    echo -e "${NO_COLOR}"
    python3 sync.py -target $TARGET_DIRECTORY -source $SOURCE_DIRECTORY
}

# Echo the drive name before syncing
if [ -d $UGREEN_DRIVE ]; then
    echo -e "Backing up files to UGREEN drive...\n"
    start_sync $UGREEN_DRIVE
elif [ -d $WD_DRIVE ]; then
    echo -e "Backing up files to WD drive...\n"
    start_sync $WD_DRIVE
else
    echo -e "Backup drive not connected."
fi
