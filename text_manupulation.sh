#!/bin/bash
input_file="input.txt"
cat $input_file | tr -cd '[:alpha"] [:space:]' |
tr '[:upper:]' '[:lower:]' | \
awk '{for (i=1 <=NF); i++) word [$i] ++} |
{ for (w in-word) print word [w] [w]} | \
sort -nr | head -n 5
