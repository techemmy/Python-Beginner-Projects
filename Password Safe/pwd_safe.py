users = {}

try:
	with open('users.txt', 'r') as f:
		for user in f:
			username, pwd = user.split(',')
			users[username] = pwd
except FileNotFoundError:
	with open('users.txt', 'w'):
		pass

while True:
	username = input("Enter your username or username to add:")
	user = users.get(username)
	if user:
		print("Password is:", user)
	elif username:
		print("User doesn't exist!")
		pwd = input("Enter password for new user:")
		print("Adding user to db")
		users[username] = pwd
		with open('users.txt', 'a') as f:
			f.write(f"{username},{pwd}\n")
		print("User added!")
