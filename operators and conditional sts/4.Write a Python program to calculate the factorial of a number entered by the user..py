#4.Write a Python program to calculate the factorial of a number entered by the user.

factorial = 1
num = int(input("Enter the number: "))

if num < 0:
    print("Factorial does not exist for negative values")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i  # Multiply factorial by i in each iteration

    # Print the final factorial after the loop
    print(factorial)
