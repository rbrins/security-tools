#!/bin/bash

# just debugging values, comment or delete out
echo "First 3 Octets:                  $1"
echo "Starting value last Octet:       $2"
echo "Ending value last Octet:         $3"

for i in $(seq $2 $3)
do
    IPADDR="$1.$i"
    OUTPUT=$(ping -c 1 $IPADDR)
    FOUND=$(echo $OUTPUT | grep -i "bytes from")
    
    if [ ! -z $FOUND ]
    then
	echo "$IPADDR"
    fi
done

