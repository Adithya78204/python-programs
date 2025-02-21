#1.Python program to find the size of a tuple.py
import sys
my_tuple = [2,3,4,5,6,7]
print(sys.getsizeof(my_tuple))

my_tuple =(2,3,4,5,6)
print(my_tuple.__sizeof__())