dict = {"'HuEx": [1, 3, 4], "is": [7, 6], "best": [4, 5]}
outer_lis = []

for key in dict:
    inner_lis = []
    inner_lis.append(key)
    inner_lis = inner_lis + list(dict[key])

    outer_lis.append(inner_lis)

print(outer_lis)