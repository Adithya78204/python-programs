#8.Program to remove all elements in a range from the List
def main():
    my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(my_list)

    start_index = 3
    end_index = 7

    # using slicing
    del my_list[start_index:end_index]

    print(my_list)

if __name__ == "__main__":
    main()

