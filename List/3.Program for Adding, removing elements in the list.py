#3.Program for Adding, removing elements in the list
list1 = [2,3,4,5,6,7,8]
print(list1)
list1.append(9)
print(list1)
list1.remove(4)
print(list1)


list = []
list.append('banana')
list.append('cherry')
print(list)

list.insert(0,'apple')
print(list)

list.remove('banana')
print(list)

my_list = []
for i in range (1,10):
    my_list.append(i)
print(my_list)

for i in my_list[:]:
    if i%2 == 0:
        my_list.remove(i)
print(my_list)




