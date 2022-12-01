#!/bin/bash

echo "Enter the first file"

read file1

echo "Enter the second file"
read file2

if cmp -s $file1 $file2
then
    echo "the contents of given files file1 and file2 are same!!!"
    rm -rf $file2
    echo "Second file deleted"

else
    echo "the contents of file1 and file 2 are different!!!"
fi