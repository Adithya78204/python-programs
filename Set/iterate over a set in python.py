#2.iterate over a set in python

my_set = {2,3,4,5,6,7}

for item in my_set:
    print(item)

#using while loop

my_set = {10, 20, 30, 40, 50}
iterator = iter(my_set)  # Create an iterator for the set

while True:
    try:
        item = next(iterator)  # Get the next item
        print(item)
    except StopIteration:
        break  # Exit loop if dont have elements



