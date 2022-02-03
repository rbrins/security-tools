#!/bin/bash

# simple tool to automate hash identification and passing to hashcat
# author: Russell Brinson
# arguments is just the hash

hash="$1"

hashid -m $hash | grep "Hashcat Mode" | cut -d":" -f 2 | cut -d"]" -f 1 > .tmpHashids
hcID=$(head -n 1 .tmpHashids)
rm .tmpHashids
hashcat -m $hcID $hash /usr/share/wordlists/rockyou.txt
