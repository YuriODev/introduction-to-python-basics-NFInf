# Exercise 4

n = int(input("Enter a 4 digit number, if it's symetric I'll lyk: "))

digit1 = n // 1000
digit2 = (n % 1000) // 100
digit3 = (n % 100) // 10
digit4 = n % 10

result = (digit1 == digit4) * (digit2 == digit3)
print(result)
