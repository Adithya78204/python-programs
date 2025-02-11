#2.Python program for adding a Tuple to List and Vice-Versa
my_list = [2,4,6]
my_tuple = (8,10,12)
my_list.extend(my_tuple)
print(my_list)


my_list = ["adhi", "pavan", "tarak"]
my_tuple = ("venu", "vamsi", "naren")
my_list = my_list + list(my_tuple)
print(my_list)

my_list = ["adhi", "pavan", "tarak"]
my_tuple = ("venu", "vamsi", "naren")
for item in my_tuple:
    my_list.append(item)
print(my_list)