#3.Write a Python program to swap the values of two variables without using a temporary variable.
a = int(input("enter the number:"))
b = int(input("enter the number:"))

a, b = b, a
print(a, b)

#using temparary value

# Get user input
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

temp = a
a = b
b = temp

print(a, b)

