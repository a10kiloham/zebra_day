#!/bin/bash

# Network range (modify if needed)
network="192.168.1"

# Loop through each IP and use curl
for i in {1..254}; do
    ip="$network.$i"
    # Use curl to fetch the page and grep to check for "Zebra"
    if curl -m 4 -s "http://$ip:80" | grep -q "Zebra"; then
        echo "$ip contains Zebra"
    fi
done