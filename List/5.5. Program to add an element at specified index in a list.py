#5.5. Program to add an element at specified index in a list
my_list = [2,4,6,8,12]
print(my_list)
my_list.insert(4, 10)
print(my_list)


def main():
    my_list = ["apple", "banana", "cherry"]
    print( my_list)

    index = 1
    new_element = "orange"

    my_list.insert(index, new_element)

    print(my_list)
if __name__ == "__main__":
    main()
