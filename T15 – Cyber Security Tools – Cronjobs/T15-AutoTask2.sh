#!/bin/bash

# Check today if it is Friday the 13th
if [[ $(date +%d) -eq 13 && $(date +%u) -eq 5 ]]; then
    /usr/bin/sudo /sbin/shutdown -r now
fi