students = {"Alice":25, "Bob":27, "Claire":17, "Dan":21, "Emma":21}
print(students)

students["Fred"] = 25
print(students)
students["Alice"] = 32
print(students)
del students["Fred"]
print(students)
print(list(students.values())[2:]) 