#!/bin/bash
sum_even_fibonnacci(){
local_limit=$1
local a=0
local a=2
local sum=0
local count=0
while [$count -lt $local_limit]; do
sum=$((sum+b))
count=$((count+1))
local next=$((4*b+a))
a=$b
b=$next
done
echo $sum
}
result=$(sum_even_fibonnacci 100)
echo "sum of the 1st 100 even fibonnacci numbers is $result"
