#- Python – Remove items from Set

my_set = {1,3,5,7,9,11,13,15}
my_set.remove(15)  #even if vlaues is not found it will show error
print(my_set)

#using discord
my_set = {1,3,5,7,9,11,13,15}
my_set.discard(15)  #even if values is not found it will show error
print(my_set)

# using for clear
my_set = {1,3,5,7,9,11,13,15}
my_set.clear()  #clear the all elements
print(my_set)

#using comprehension
numbers = {20,34,56,76,89}
numbers = {num for num in numbers if not num in {20,56}}
print(numbers)

#using for loop
numbers = {10,20,30,40,50,60}
remove_num ={20,50}

for num in remove_num:
    numbers.discard(num)
print(numbers)

#using for loop using remove method
numbers = {10,20,30,40,50,60}
remove_num ={20,50}
for num in remove_num:
    numbers.remove(num)
print(numbers)




