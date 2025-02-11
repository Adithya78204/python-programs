#4.Python program to create a list of tuples from given list having number and its cube in each tuple.py
def create_cube_tuples(numbers):
    result = []
    for num in numbers:
        result.append((num, num*3))
    return result
num_list = [1,2,3,4,5]
cube_num = create_cube_tuples(num_list)
print(cube_num)