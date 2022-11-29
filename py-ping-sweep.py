#!/bin/python3

# Create a wrapper around ping using python instead of bash, with input checking

import os
import argparse

parser = argparse.ArgumentParser(
    prog = "Python Ping Sweep",
    description = "Python wrapper around ping utility")

parser.add_argument('firstOctet')
parser.add_argument('starting', type=int, metavar="[1-255]")
parser.add_argument('ending', type=int, metavar="[1-255]")

args = parser.parse_args()

# Sanitize inputs
tmp_firstOctet = args.firstOctet.split(".")

if (len(tmp_firstOctet) != 3):
    exit(1)
s_firstOctet = args.firstOctet

# still should check the firstOctet if in the range of 1-255

if (args.ending < args.starting):
    print("Ending IP Address must be higher than starting")
    exit(1)
else:
    s_starting = args.starting
    s_ending = args.ending


pingCmd_front = "ping -c 1 "
pingCmd_end = " >/dev/null"

for i in range(s_starting, (s_ending + 1)):
    host = s_firstOctet + "." + str(i)
    pingCmd = pingCmd_front + host + pingCmd_end
    response = os.system(pingCmd)
    if (response == 0):
        print(host)

