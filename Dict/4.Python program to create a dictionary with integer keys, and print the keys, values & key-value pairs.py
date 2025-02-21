#4.Python program to create a dictionary with integer keys, and print the keys, values & key-value pairs

num_dict = {1:"one", 2:"two", 3:"three"}
print("keys:", num_dict.keys())
print("values:", num_dict.values())
print("key-value pairs:")
for keys, values in num_dict.items():
    print(keys, ":" ,values)