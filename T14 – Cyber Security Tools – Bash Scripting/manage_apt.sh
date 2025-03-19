#!/bin/bash

# Check if the script is running
if [ "$EUID" -ne 0 ]; then
    echo "Error: This script must be run as root."
    exit 1
fi

echo "Starting APT package management tasks..."

# Uninstall all unused dependencies
apt autoremove

# Update the software package database
apt update

# Upgrade the entire system
apt upgrade

echo "APT tasks completed successfully."