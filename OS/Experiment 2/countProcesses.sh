# write a code using shell script that counts the number of processes running on the system
# and prints the result on the screen.

numProcessess=$(ps -e | wc -l)
echo "The number of processes running on the system is : " $(ps -e | wc -l)
echo "The number of processes running on the system is : $numProcessess" 



