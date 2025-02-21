#5.Write a Python program to check if a year entered by the user is a leap year or not.

year = int(input("enter the year:"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("it is leap year")
else:
    print("it is not leap year")