#4.Write a Python program to print the Fibonacci series up to n terms using a while loop.
#example :- 0 1 2 3 5 8 13 21......n
num1 = 0
num2 = 1
n = int(input("enter the number:"))
print(num1, end=" ")
print(num2, end=" ")
for i in range (2, n+1):
    num3 = num1 + num2
    print(num3, end=" ")
    num1 = num2
    num2 = num3

#using while loop

num1 = 0
num2 = 1
n = int(input("enter the number:"))

if n == 0:
    print()  # Handle the case where n is 0 (print nothing)
elif n == 1:
    print(num1)  # Handle the case where n is 1 (print only num1)
else:
    print(num1, end=" ")
    print(num2, end=" ")

    count = 2  # Initialize count to 2 (since we've already printed 2 numbers)
    while count < n:
        num3 = num1 + num2
        print(num3, end=" ")
        num1 = num2
        num2 = num3
        count += 1
