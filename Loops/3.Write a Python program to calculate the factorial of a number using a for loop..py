#3.Write a Python program to calculate the factorial of a number using a for loop.

num = int(input("enter the numbers:"))
if num < 0:
    print("negative numbers not defined")
elif num == 0:
    print("factorial of 0 is 1")
else:
    result = 1
    for i in range(1, num+1):
        result *= i
    print(f"factorial of {num} is:", result)

