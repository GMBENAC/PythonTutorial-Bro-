
friends = 10
#friends = friends + 1
#friends += 1
#friends = friends - 2
#friends -= 2
#friends = friends * 3
#friends *= 3
# friends = friends / 3
#friends /= 2
#friends = friends ** 2
#friends **= 2
#reminder = friends % 4
# print(reminder)

x = 3.14
y = -4
z = 5

#result = round(x)
#result = abs(y)
#result = pow(4, 3)
#result = max(x, y, z)

import math

w = 9.9

print(math.pi)
print(math.e)

result = math.sqrt(w)

print(result)

# Ecercise 1 Circcunference and Circle Area

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)

print(f"The circumference is: {round(circumference, 2)} cm")
print(f"The area of the circle is: {round(area, 2)} cm²")

# Hypotenuse of a right triangle

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side c = {c}")
