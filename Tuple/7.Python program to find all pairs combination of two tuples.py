def pair_combination(tuple1, tuple2):
    pairs = []

    for item1 in tuple1:
        for item2 in tuple2:
            pairs.append((item1,item2))
    return pairs
tuple1 = (2,4)
tuple2 = (5,6)
result = pair_combination(tuple1,tuple2)
print(result)