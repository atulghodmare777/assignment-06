#!/bin/bash
input_file="input.txt"

# Process the text: remove non-alphabetic characters, convert to lowercase, count word occurrences, and find top 5 words
cat "$input_file" | tr -cd '[:alpha:][:space:]' | tr '[:upper:]' '[:lower:]' |
awk '{for (i=1; i<=NF; i++) word[$i]++} END {for (w in word) print word[w], w}' |
sort -nr | head -n 5
