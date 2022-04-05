lis = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]]

for inner_lis in lis:
    dict = {}
    for item in inner_lis:
        if item in dict:
            dict[item] = dict[item] + 1
        else:
            dict[item] = 1

    for key in dict:
        if dict[key] > 1:
            print(key, "->", dict[key])
