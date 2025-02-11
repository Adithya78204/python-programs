#9. Program to sort the elements of given list in Ascending and Descending Order
# my_list = [3,2,6,4,9,5,8,9]
# list.sort(my_list)
# print(my_list)

def sort_list (numbers):
    ascending = sorted(numbers)
    descending = sorted(numbers, reverse=True)

    print(numbers)
    print(ascending)
    print(descending)

list = [2,3,5,4,7,8,5,6,7]

sort_list(list) #calling function
