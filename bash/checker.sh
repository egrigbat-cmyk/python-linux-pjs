#!/bin/bash
DISK=$(df / | grep "/" | awk '{print $5}' | sed 's/%//')
if [ $DISK -gt 80 ]; then
   echo "WARNING: Disk usage is at ${DISK}%"
else
   echo "Disk is ok: ${DISK}%"
fi
