import math
print("This program calculates the area and circumference of a circle")

radius = float (input("Write the radius: "))
area = math.pi * (radius ** 2)
circum = 2 * math.pi * radius

print("Area: ", round(area,4))
print("Circumference: ", round(circum,4))

