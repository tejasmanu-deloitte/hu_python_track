dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {}


def merge_dict(dict):
    for key in dict:
        if key in dict3:
            continue
        else:
            dict3[key] = dict[key]


merge_dict(dict1)
merge_dict(dict2)

print(dict3)
