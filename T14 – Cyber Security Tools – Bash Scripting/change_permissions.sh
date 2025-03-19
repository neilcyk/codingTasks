#!/bin/bash

# Define the target directory
TARGET_DIR="my_folder"

# Check if the directory exists
if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: Directory '$TARGET_DIR' does not exist."
    exit 1
fi

# Change permissions of all files and directories using symbolic mode
find "$TARGET_DIR" -exec chmod u=rw,go=r {} \;

echo "Permissions changed to -rw-r--r-- for all objects in '$TARGET_DIR'."