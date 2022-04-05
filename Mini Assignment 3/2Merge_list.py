list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
final_list = list()

for element in list1:
    for element1 in list2:
        final_list.append(element+element1)

print(final_list)