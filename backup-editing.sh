#!/bin/bash

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

echo -e "Finding backup drive path...\n"
DRIVE=$(find /media/t-visor -name 'my-files')

# start syncing if the drive is connected 
[ ! -z $DRIVE ] && start_sync $DRIVE || echo "Drive not connected."
