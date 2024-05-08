# Exercise 1
number = int(input("Enter a 5 digit number"))
# Extracting the digits
digit1 = number // 10000
print(f"{digit1 = }")
digit2 = number // 1000 % 10
print(f"{digit2 = }")
digit3 = number // 100 % 10
print(f"{digit3 = }")
digit4 = number // 10 % 10
print(f"{digit4 = }")
digit5 = number // 1 % 10
print(f"{digit5 = }")
# Printing the digits
first_int = str(digit1 + digit3 + digit5)
second_int = str(digit2 + digit4)
skib = (first_int + second_int)
print(skib)