#5.Python program to create a dictionary with mixed keys, and print the keys, values & key-value pairs
mixed_dict = {
    1 : "one",
    "name" : "adithya",
    2.3 : "float"
}
print("keys:", mixed_dict.keys())
print("values:", mixed_dict.values())
print("key-vlaue pairs:")
for keys, values in mixed_dict.items():
    print(keys, ":",values)