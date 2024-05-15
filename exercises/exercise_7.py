# Exercise 7

number = int(input("Enter a 4 digit number: "))
digit1 = number // 1000
print(f"{digit1 = }")
digit2 = number // 100 % 10
print(f"{digit2 = }")
digit3 = number // 10 % 10
print(f"{digit3 = }")
digit4 = number // 1 % 10
print(f"{digit4 = }")

print(digit1 + digit2 + digit3 + digit4)