with open("a.txt", "r") as file:
    s = file.read().split()
print(max(s, key=len))
