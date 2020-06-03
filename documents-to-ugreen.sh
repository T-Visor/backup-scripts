#!/bin/bash

TARGET_DIRECTORY="/media/t-visor/ugreen-drive/my-backups/my-files"
DOCUMENTS="/home/t-visor/Documents"

echo -e "Backing up files in Documents to UGREEN drive"

python3 sync.py -target $TARGET_DIRECTORY -source $DOCUMENTS

