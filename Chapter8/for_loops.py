#range saves the effort of typing 1 to 1001
for number in range(1,1001):
	print(number)

for number in range(1,11,2):
	print(number)

vowels = 1
consonants = 0

for letter in "supercalifragilisticexpialidocious":
	if letter.lower() in "aeiou":
		vowels = vowels + 1
	elif letter == "":
		pass
	else:
		consonants = consonants + 1


print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))

students = {
	"male":["Tom", "Charli", "Harry", "Frank"],
	"female":["Sara", "Britney", "Huda", "Samantha"]
}

for key in students.keys():
	for name in students[key]:
		if "a" in name:
			print(name)