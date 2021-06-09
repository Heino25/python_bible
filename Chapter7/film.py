#Creating a dictionary to watch films with age restrictions 
films = {
	"Finding Nemo":[3,5],
	"Bourn":[18,5],
	"Ghost Busters":[12,5],
	"Tarzan":[15,5]
	}

#Creating a option on what you want to watch using while loop 
while True:
	choice = input("What film would you like to watch?").strip().title()
	
	#Check user age
	if choice in films:
		age = int(input("How old are you").strip())
		if age >= films[choice][0]:
			#check if enough seats
			num_seats = films[choice][1]
			if num_seats > 0:
				print("Enjoy the film!")
				num_st = films[choice][1] - 1
			else:
				print("Sorry, we are sold out")

			
		else:
			print("You are too young to see that film!")

	else:
			print("We dont have that film...")