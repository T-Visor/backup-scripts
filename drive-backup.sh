#!/bin/bash

TARGET_DIRECTORY=value
SOURCE_DIRECTORY="/home/t-visor/Documents"

# Console text colors
RED='\033[1;33m'
PURPLE='\033[1;35m'
NO_COLOR='\033[0m'

if [ -d "/media/t-visor/ugreen-drive/my-backups/my-files" ]; then
    TARGET_DIRECTORY="/media/t-visor/ugreen-drive/my-backups/my-files"
    echo -e "Backing up files to UGREEN drive... "
    echo -e ""
    echo -e "${RED}SOURCE: $SOURCE_DIRECTORY"
    echo -e "${PURPLE}DESTINATION: $TARGET_DIRECTORY"
    echo -e "${NO_COLOR}"
    python3 sync.py -target $TARGET_DIRECTORY -source $SOURCE_DIRECTORY
elif [ -d "/media/t-visor/wd-drive/my-backups/my-files" ]; then
    TARGET_DIRECTORY="/media/t-visor/wd-drive/my-backups/my-files"
    echo -e "Backing up files to WD drive... "
    echo -e ""
    echo -e "${RED}SOURCE: $SOURCE_DIRECTORY"
    echo -e "${PURPLE}DESTINATION: $TARGET_DIRECTORY"
    echo -e "${NO_COLOR}"
    python3 sync.py -target $TARGET_DIRECTORY -source $SOURCE_DIRECTORY
else
    echo -e "Backup drive not connected."
fi
