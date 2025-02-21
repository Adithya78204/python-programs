#6.Python | Generate dictionary of numbers and their squares (i, i*i) from 1 to N

def generate_squares(n):
    return {i: i*i for i in range(1, n+1)}
N = int(input("enter the numbers:"))
suare_dict = generate_squares(N)
print(suare_dict)