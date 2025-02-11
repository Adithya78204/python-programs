#6. Program to remove first occurrence of a given element in the list

my_list = [20,40,50,10,20,70,20]
print(my_list)
my_list.remove(20)
print(my_list)


def main():
    my_list = [10, 20, 30, 20, 40, 20, 50]
    print(my_list)
    element_remove = 20
    if element_remove in my_list:
        my_list.remove(element_remove)
        print( my_list)
    else:
        print(element_remove)

if __name__ == "__main__":
    main()

