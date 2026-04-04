#!/bin/bash

ports=(21 22 23 80 443)

for port in "${ports[@]}"; do
   if ss -tuln | grep -q ":$port "; then
     echo "$port is open"
   else
     echo "$port is closed"
   fi
done
