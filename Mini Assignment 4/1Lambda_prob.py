def prob1(a, b, c, x):
    soln = lambda a, b, c, x: (a * (x ^ 2)) + (b * x) + c

    return soln(a, b, c, x)


def prob2():
    lst1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

    result = list(map(lambda x: (x.count("a") + x.count("A")), lst1))

    return result


print("Solution : ", prob1(2, 5, 4, 2))

print("The number of occurrences of 'a' or 'A' is : ", prob2())
