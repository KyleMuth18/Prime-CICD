#!/bin/bash
cd /home/ubuntu/prime
chmod +x prime.py
python3 prime.py 5 > output.txt 2>&1
echo "Script executed at $(date)" >> debug.log

