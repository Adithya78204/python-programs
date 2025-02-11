#3.Python program to create a dictionary from a sequence

keys = ["name", "age", "course"]
values = ["adhi", 24, "MCA"]

student = dict(zip(keys, values))
print(student)