#2.Write a Python program to print all even numbers between 1 and 20 using a while loop.

for i in range(1, 20+1):
    if i % 2 == 0:
        print(i, end = " ")

#using while loop

numbers = 1
while numbers <= 20+1:
    if numbers % 2 == 0:
        print(numbers)
    numbers += 1