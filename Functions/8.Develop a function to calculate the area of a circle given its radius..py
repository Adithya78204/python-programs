#8.Develop a function to calculate the area of a circle given its radius.
import math
def area_of_circle(radius):
    return math.pi * radius ** 2  #pi = 3.14159

radius = int(input("enter the radius:"))
print(area_of_circle(radius))