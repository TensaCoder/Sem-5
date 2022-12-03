# write a code to count number of users logged in the system and print the result on the screen.

# !/bin/bash

echo "The number of users logged in the system is : " $(who | wc -l)