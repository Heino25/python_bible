known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]
print(len(known_users))

while True:
	print("Hi! My Name is Travis")
	name = input("What is your name?:").strip().capitalize()

	if name in known_users:
		print("Hello {}!".format(name))
		remove = input("Would you like to be removed from the system (y/n)?:").lower()
		
		if remove == "y":
			print(known_users)
			known_users.remove(name)
			print(known_users)
	else:
		print("Name NOT recognised")	