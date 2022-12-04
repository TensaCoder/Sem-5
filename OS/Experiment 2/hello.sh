# !/bin/zsh
#thuis is a comment
# echo $SH
# echo $BASH
# echo $ZSH
# echo $PATH

# echo $ZSH_VERSION
# echo $BASH_VERSION


# read name
# echo "the entered name is : $name"

echo "Enter a number: "
read number
num=$number
fact=1 
while [ $number -gt 1 ]
do 
fact=$((fact*number))
number=$((number-1))
done
echo "The factorial of $num  with while loop: $fact"


fact=1
for ((i=$num; i>1; i--))
do
fact=$((fact*i))
done
echo "The factorial of $num  with for loop: $fact"
