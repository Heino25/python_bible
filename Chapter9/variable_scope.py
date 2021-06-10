a = [1,2,3]

def f1():
	a[0] = 5
	a[2] = "Hi"
	print(a)

def f2():
	a = 50 # local
	print(a)

f1()
f2()
