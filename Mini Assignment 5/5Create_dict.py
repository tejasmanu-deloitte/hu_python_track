lst1=["Netflix", "Hulu", "Sling", "Hbo"]
lst2=[198, 166, 237, 125]
if len(lst1) != len(lst2):
    print("Number of Keys and values are not same")
else:
    result = dict(zip(lst1,lst2))
print(result)