#!/bin/bash

##################################################################
# Description: Search for a designated folder name               #
#              in an external drive and start the backup process #
#              if found. This script calls a Python script       #
#              named 'sync.py' which will handle the rest of     #
#              the backup process.                               #
#                                                                #
# Author: T-Visor                                                #
##################################################################

# Designated directory name for storing backups 
BACKUP_FOLDER='my-files'

# Source and target directories for backup
# 'TARGET_DIRECTORY' value is dependent on which drive is connected 
TARGET_DIRECTORY=value
SOURCE_DIRECTORY="/home/t-visor/Documents"

# Console text colors
RED='\033[1;33m'
PURPLE='\033[1;35m'
NO_COLOR='\033[0m'

echo -e "Finding backup drive path...\n"
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
