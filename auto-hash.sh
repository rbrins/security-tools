#!/bin/bash

# simple tool to automate hash identification and passing to hashcat
# author: Russell Brinson
# arguments is just the hash
#
# Future Todos:
# [ ] more information, 
#   [ ] hash regurgitated for debugs
#   [ ] help menu
#   [ ] pretty ascii art
# eventually I want it to display some more information, not show the hashcat dump, 
# and to have the option to pause and allow for selection of the hash type, or to cycle through them all, then a flag to pass the onerules

hash="$1"

hashid -m $hash | grep "Hashcat Mode" | cut -d":" -f 2 | cut -d"]" -f 1 > .tmpHashids
hcID=$(head -n 1 .tmpHashids)
rm .tmpHashids
hashcat -m $hcID $hash /usr/share/wordlists/rockyou.txt