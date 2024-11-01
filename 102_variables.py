# This is my first program

print("I like pizza!")
print("It`s really good!")

# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the valeu contains

# Strings

first_name = "Gabriel"
food = "pork"
email = "benacmgabriel@gmail.com"

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

# Integers 
age = 36
quantity = 3
num_of_students = 30

# Float
price = 10.99
gpa = 3.2
distance = 5.5

# Boolean 

is_student = False
for_sale = True
is_online = True



print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")
print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance} Km")
print(f"Are you a student?: {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT available")
if is_online:
    print("You are online")
else:
    print("You are offline")
