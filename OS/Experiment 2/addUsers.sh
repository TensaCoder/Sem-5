userFile=/userList.txt

usernames=$(cat userList.txt)
password=password@123

for user in $usernames
do
	useradd $user
	echo $password
done
echo "$(wc -l userList.txt) user have been created"
