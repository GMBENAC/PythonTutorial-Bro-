
# name = input("Enter your full name: ")
# phone_number = input("Enter your phone number: ")

#result1 = len(name)
#print(result1)
#result2 = name.find("o")
#print(result2)
#result3 = name.rfind("q")
#print(result3)
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("-")
# result = phone_number.replace("-"," ")
# result = phone_number.replace("-","")

# print(result)

# print(help(str))

# validate user input exercise
# 1. username is no more than 12 characteres
# 2. user must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")


if len(username) > 12:
    print("Your username can`t be more than 12 characteers")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can`t contain numbers")
else:
    print(f"Welcome {username}")



