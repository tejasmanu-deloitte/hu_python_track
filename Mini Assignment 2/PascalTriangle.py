n = int(input("input - "))

for i in range(n):
    print(11 ** i, end="")
    for j in range(n - i):
        print(0, end="")

    print()
