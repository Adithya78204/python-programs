# Find the size of a Set in Python

my_set = {2,3,4,5,6,7}
print(len(my_set))

#if you give duplicate elements it will not find the length
my_set = {3,4,5,6,3,5,7,8,3}
print(len(my_set))

#using for loop
my_set = {3,4,5,6,7,8}
count = 0

for item in my_set:
    count +=1
print("count size is:",count)


