# Exercise 9
hours = int(input("How many hours have passed today: "))
minutes = int(input("How many minutes have passed today: "))

degrees = hours * (360/12)
if minutes > 0:
    degrees += minutes * (360/60/12)
if degrees > 360:
    degrees = degrees - 360
    print("The Hour hand has turned", degrees, "degrees")
else:
    print("The Hour hand has turned", degrees, "degrees")
    