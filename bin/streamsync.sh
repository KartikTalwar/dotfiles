#!/bin/sh

#TODO:
# 1. support file paths and names in all arguments
# 2. replace .* with a more specific list of extensions

while [ -e "$1.*" ]; do
	rsync --inplace --progress "$1.*" "$2"/`basename "$1"`
	if [ -z $3 ]; then
		sleep $3
	else
		sleep 10
	fi
done
rsync --inplace --progress "$1" "$2"/`basename "$1"`
