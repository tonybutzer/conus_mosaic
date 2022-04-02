#! /bin/bash

FILE=~/token.txt
if test -f "$FILE"; then
    echo "$FILE exists."
    cat $FILE
fi

