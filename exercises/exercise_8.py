# Exercise 8
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

min_value = num1 * (num1 <= num2 and num1 <= num3) + num2 * (num2 < num1 or num2 < num3) + num3 * (num3 < num1 and num3 < num2)
max_value = num1 * (num1 >= num2 and num1 >= num3) + num2 * (num2 > num1 or num2 > num3) + num3 * (num3 > num1 and num3 > num2)
mid_value = num1 + num2 + num3 - min_value - max_value

print(min_value)
print(mid_value)
print(max_value)