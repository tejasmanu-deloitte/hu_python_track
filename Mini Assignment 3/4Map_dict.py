Keys = ["Ten", "Twenty", "Thirty"]
Value = [10,20,30]
dict = {}

if(len(Keys)!=len(Value)):
    print("Number of keys and values do not match")

for index in range(len(Keys)):
    dict[Keys[index]] = Value[index]

print(dict)