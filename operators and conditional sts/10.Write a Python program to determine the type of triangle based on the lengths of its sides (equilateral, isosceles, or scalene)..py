#10.Write a Python program to determine the type of triangle based on the lengths of its sides (equilateral, isosceles, or scalene).
def determine_triangle_type(a, b, c):
    if a == b == c:
        print("The triangle is Equilateral.")
    elif a == b or b == c or a == c:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")

# Taking input from the user
side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

# Checking if valid triangle
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    determine_triangle_type(side1, side2, side3)
else:
    print("The given sides do not form a valid triangle.")
