# Exercise 3
n = int(input("Enter a number of seconds"))

# Calculate the hours, minutes, and seconds
h = (n // 3600) % 24
m = (n // 60) % 60
s = n % 60

# Print the time in h:mm:ss format
print(f"{h}:{m:02d}:{s:02d}")