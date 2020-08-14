#!/bin/bash

BACKUP_FOLDER='my-files'

# Source and target directories for backup
# 'TARGET_DIRECTORY' value is dependent on which drive is connected 
TARGET_DIRECTORY=value
SOURCE_DIRECTORY="/home/t-visor/Documents"

# Console text colors
RED='\033[1;33m'
PURPLE='\033[1;35m'
NO_COLOR='\033[0m'

echo -e "Finding '$BACKUP_FOLDER' on external drive...\n"
backup_path=$(find /media/t-visor -maxdepth 3 -name $BACKUP_FOLDER) 

start_sync () {
    TARGET_DIRECTORY=$1
    echo -e "${RED}SOURCE: $SOURCE_DIRECTORY"
    echo -e "${PURPLE}DESTINATION: $TARGET_DIRECTORY"
    echo -e "${NO_COLOR}"
    python3 sync.py -target $TARGET_DIRECTORY -source $SOURCE_DIRECTORY
}

# Start syncing if the drive is connected 
[ ! -z $backup_path ] && start_sync $backup_path || echo "Drive not connected."
