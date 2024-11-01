# logical operators = evaluate multiple conditions (or, and, not)

#                     or = at least one condition must be True
temp1 = 36
is_raining = False

if temp1 > 35 or temp1 < 0 or is_raining:
    print("The outdorr event is cancelled")
else:
    print("The outdoor event is still scheduled")

#                     and = both conditions must be True
temp2 = 20
is_sunny = True

if temp2 >= 28 and is_sunny:
    print("It is HOT outside 🥵")
    print("It is SUNNY 🌞")
elif temp2 <= 0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY 🌞")
elif 28 > temp2 > 0 and is_sunny:
    print("It is WARM outiside 😀")
    print("It is SUNNY 🌞")

#                     not = inverts the condition (not False, not True)

temp3 = 20
is_sunny = False

if temp3 >= 28 and not is_sunny:
    print("It is HOT outside 🥵")
    print("It is SUNNY ⛅")
elif temp3 <= 0 and not is_sunny:
    print("It is COLD outside 🥶")
    print("It is CLOUDY ⛅")
elif 28 > temp3 > 0 and not is_sunny:
    print("It is WARM outiside 😀")
    print("It is CLOUDY ⛅")
