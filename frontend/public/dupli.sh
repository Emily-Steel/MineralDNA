#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <file_to_copy>"
    exit 1
fi

targets_file=./targets.txt
file_to_copy=$1

# Check if the destination file exists
if [ ! -f "$targets_file" ]; then
  echo "Error: Targets file '$targets_file' does not exist."
  exit 1
fi

# Check if the file to copy exists
if [ ! -f "$file_to_copy" ]; then
  echo "Error: File to copy '$file_to_copy' does not exist."
  exit 1
fi

# Read each line of the destination file and copy the predefined file to that location
while IFS= read -r destination; do
  if [ -n "$destination" ]; then
    echo "Copying '$file_to_copy' to '$destination'..."
    cp "$file_to_copy" "$destination" || echo "Failed to copy to '$destination'"
  fi
done < "$targets_file"

echo "Copy operation complete."