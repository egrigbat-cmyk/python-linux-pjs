#!/bin/bash

ips=("192.168.1.1" "8.8.8.8" "192.168.1.2")

for ip in "${ips[@]}"; do
  if ping -c 1 $ip > /dev/null 2>&1; then
     echo "$ip is reachable"
  else
     echo "$ip is not reachable"
  fi
done
