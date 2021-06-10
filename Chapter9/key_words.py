def about(name, age, likes):
	sentence = "Meet {}!\nHe is {} years old and they like{}".format(name, age, likes)
	return sentence

print(about("Jack", 23, "Python"))	
print(about(age = 23, name = "Jack", likes = "Python"))

