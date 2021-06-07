#Get user email address
email = input("What is your email address?:").strip()
#Slice out user name
user = email[:email.index("@")]
#slice domain name
domain = email[email.index("@") + 1:]
#format message
string = "Your username is {} and your domain name is {}".format(user, domain)
#disply output message
print(string)
