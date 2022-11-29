#!/bin/bash

# extract file types from a log

# Default values and debugging info
FILEEXT=${2:-"js"}
TMPFILELOC=${3:-"/tmp/extractingdump.txt"}
echo "Log Location:            $1"
echo "Default File ext:        $FILEEXT"
echo "Temporary File Location: $TMPFILELOC"

# with line anchors ^ and $ (escaped with \) 
# Just looking at file that start with forward slash (may need to add or other special characters)
REGEX="/.\.*$FILEEXT"

cat $1 | while read line
do
    # double rev is like reverse reverse in code thanks stackoverflow https://stackoverflow.com/questions/22727107/how-to-find-the-last-field-using-cut for the idea
    FOUND=$( echo $line | grep -oe $REGEX | rev | cut -d'/' -f1 | rev )

    if [ ! -z "$FOUND" ]
    then
	echo "$FOUND" >> "$TMPFILELOC"
    fi
done

# Make this tmp file a variable with default tmp
sort -u "$TMPFILELOC"
rm "$TMPFILELOC"
