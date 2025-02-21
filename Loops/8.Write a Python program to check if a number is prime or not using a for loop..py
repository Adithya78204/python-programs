#8.Write a Python program to check if a number is prime or not using a for loop.

num = int(input("enter the number:"))

count = 0
if num > 1:
    for i in range(1, num+1):
        if num % i == 0:
            count = count + 1
        if count == 2:
            print("it is prime")
        else:
            print("it is not prime")