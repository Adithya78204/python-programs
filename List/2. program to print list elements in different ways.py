#2. program to print list elements in different ways
# my_list = [2,3,5,6.5, "adhi"]
# print(my_list)
#
# for i in my_list:
#     print(i, end=" ")

#using join method
my_list = ['apple', 'banana', 'cherry']
print(', '.join(my_list))
z
#using list comprehension
my_list=[2,3,4,5,6,7,8]
[print(item) for item in my_list]

#using map() function
my_list = [2,3,4,5,6,7,8,9]
list(map(print, my_list))

