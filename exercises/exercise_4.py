# Exercise 4
# Read the input
n = int(input("Enter a 4 digit number, if it's symetric I'll lyk: "))

# Extract the digits
digit1 = n // 1000
digit2 = (n % 1000) // 100
digit3 = (n % 100) // 10
digit4 = n % 10

# Calculate the result
result = (digit1 == digit4) * (digit2 == digit3)

# Print the result
print(result)
