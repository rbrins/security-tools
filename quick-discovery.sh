#!/bin/bash

# simple tool to automate:
#   host discovery through ping sweep and arp scan then correlate
#   rescan with host-up flag to determine ports open
# 
# input: 
#   network range to be scanned (i.e. 192.168.1.0/24)
#   network card (can be ID in `ip a`, only works with a mac address so not with vpns)
# TODOs:
#   [ ] input checking, an valid IP range, and interface with a network card
#   [ ] error checking on the commands

ipRange="$1"
ethCard="$2"

echo "[ ] nmap pingsweep started on $ipRange"
sudo nmap -sn $ipRange | grep "scan report" | cut -d" " -f 5 > .tmpIPadd.txt
echo "[+] nmap pingsweep completed successfully"

echo "[ ] arp-scan started on interface $ethCard"
sudo arp-scan -I $ethCard $ipRange | grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" >> .tmpIPadd.txt
echo "[+] arp-scan completed successfully"

sort .tmpIPadd.txt | uniq > IPsDiscovered.txt
echo "[+] IPsDiscovered.txt available for IP list only"

echo "[ ] nmap aggressive scan started"
sudo nmap -Pn -A -p- -iL IPsDiscovered.txt -oA IPsScanned
echo "[+] nmap results completed and available"

