price1 = 3.14159
price2 = -987.65
price3 = 12.34

# . (number)f = round to that many decimal places (fixed point)

print(f"Price 1 is ${price1:.3f}")
print(f"Price 2 is ${price2: .3f}")
print(f"Price 3 is ${price3: .3f}")

# : (number) = allocate that many spaces

print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")

# :03 = allocate and zero pad that many spaces

print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")

# :< = left justify

print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")

# :> = right justify

print(f"Price 1 is ${price1:>10}")
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}")

# ^ = center align

print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")

# :+ = use a plus sign to indicate positive value

print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")

# := = place sign to leftmost position



print(f"Price 1 is ${price1:=}")
print(f"Price 2 is ${price2:=}")
print(f"Price 3 is ${price3:=}")

# : = insert a space before positive numbers

print(f"Price 1 is ${price1: }")
print(f"Price 2 is ${price2:  }")
print(f"Price 3 is ${price3: }")

# :, = comma separator

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")




