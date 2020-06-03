#!/bin/bash

TARGET_DIRECTORY="/media/t-visor/ugreen-drive/my-backups/my-files"
SOURCE_DIRECTORY="/home/t-visor/Documents"

echo -e "Backing up files to UGREEN drive... "
echo -e "SOURCE: $SOURCE_DIRECTORY"
echo -e "DESTINATION: $TARGET_DIRECTORY"
echo -e ""

python3 sync.py -target $TARGET_DIRECTORY -source $SOURCE_DIRECTORY

