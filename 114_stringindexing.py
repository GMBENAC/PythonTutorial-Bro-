# indexing = accesing elements of sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[0:4]) 
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-1])
print(credit_number[::2])

# Exemple 1 return the last digits of a credit card number

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

# Exemple 2 reverse the numbers

credit_number1 = credit_number[::-1]
print(credit_number1)
