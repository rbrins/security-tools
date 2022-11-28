#!/bin/bash

# extract file types from a log

# Default values and debugging info
FILEEXT=${2:-".js"}
TMPFILELOC=${3:-"/tmp/extractingdump.txt"}
echo "Log Location:            $1"
echo "Default File ext:        $FILEEXT"
echo "Temporary File Location: $TMPFILELOC"

# with line anchors ^ and $ (escaped with \) 
# Just looking at file that start with forward slash (may need to add or other special characters)
REGEX="^/.*$FILEEXT\$"

cat $1 | while read line
do
    FOUND=$( echo $line | grep -e $REGEX )

    if [ ! -z $FOUND ]
    then
	echo "$FOUND" >> $TMPFILELOC
    fi
done

# Make this tmp file a variable with default tmp
sort -u $TMPFILELOC
rm $TMPFILELOC
