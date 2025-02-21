import re

nameage = "Jeevana is 25 prasanna is 29 ganesh is 30 Vamsi is 37 Ashrith is 8"
pattern = "(\w+) is (\d+)"
matches = re.findall(pattern, nameage)
result_dict = dict(matches)
print(result_dict)
