#Using count() to count e
print("hello".count("e"))
text = "happy birthday"
print(text.count("a"))
#Testing case sensitive
x = "happy Birthday"
print(x.lower())
print(x.upper())
print(x.title())
#
z = "happy birthday"
print(z.index("birthday"))
#Clear the zeros
y = "000000happybirthday000000"
print(y.strip("0"))
print(y.lstrip("0"))
print(y.rstrip("0"))
#taking away any spaces the user leaves
name = input("What is your name?").strip()
print(name)
