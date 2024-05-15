# Exercise 10
hours = int(input("How many hours have passed today: "))
minutes = int(input("How many minutes have passed today: "))

minute_hand = minutes *6
degrees = hours * (360/12)
if degrees > 360:
    degrees = degrees - 360
    print(f"The Hour Hand has rotated {degrees} degrees")
    print(f"The Minute Hand has rotated {minute_hand} degrees")
else:
    print(f"The Hour Hand has rotated {degrees} degrees")
    print(f"The Minute Hand has rotated {minute_hand} degrees")