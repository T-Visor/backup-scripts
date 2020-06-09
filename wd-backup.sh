#!/bin/bash

TARGET_DIRECTORY="/media/t-visor/wd-drive/my-backups/my-files"
SOURCE_DIRECTORY="/home/t-visor/Documents"

# Console text colors
RED='\033[1;33m'
PURPLE='\033[1;35m'
NO_COLOR='\033[0m' 

echo -e "Backing up files to WD drive... "
echo -e ""
echo -e "${RED}SOURCE: $SOURCE_DIRECTORY"
echo -e "${PURPLE}DESTINATION: $TARGET_DIRECTORY"
echo -e "${NO_COLOR}"

python3 sync.py -target $TARGET_DIRECTORY -source $SOURCE_DIRECTORY
