#7.Remove all occurrences a given element from the list.py
def main():
    my_list = [10, 20, 30, 20, 40, 20, 50]
    print(my_list)

    element_to_remove = 20

    # Create a new list that includes only elements not equal to element_to_remove
    my_list = [item for item in my_list if item != element_to_remove]
    print( my_list)
if __name__ == "__main__":
    main()

