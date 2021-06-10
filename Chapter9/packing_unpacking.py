numbers = [1,2,3,4,5]
print(numbers)
print(*numbers)
print("abc")
print(*"abc")

def about(name, age, likes):
	sentence = "Meet {}!\nHe is {} years old and they likes{}".format(name, age, likes)
	return sentence

dictionary = {"name": "Ziyad", "age":23, "likes": "Python"}
print(about(**dictionary))

def  foo(**kwargs):
	for key, value in kwargs.items():
		print("{}:{}".format(key, value).title())

foo(huda = "Female", ziyad = "male")