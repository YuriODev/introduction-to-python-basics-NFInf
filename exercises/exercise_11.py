# Exercise 11
dollars_needed = int(input("How much do you need to give: "))
hundreds = dollars_needed // 100
tens = dollars_needed // 100
ones = tens // 1
print(hundreds)
print(tens)
print(ones)