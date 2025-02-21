#3.Write a function to check if a given number is even or odd.
def check_even_odd(num):
    if num % 2 == 0:
        print("it is even")
    else:
        print("it is odd")
number = int(input("enter the number:"))
check_even_odd(number)



