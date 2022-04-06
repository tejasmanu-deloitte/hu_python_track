class FormulaError(Exception):
    pass


while True:
    opr = input("Enter the operation or enter quit to exit:")
    if opr.lower() == "quit":
        break
    lis = list(opr)

    # Check if there are 3 elements in the expression
    if len(lis) != 3:
        raise FormulaError("Enter a valid Expression")

    # Check if the operands are valid
    try:
        op1 = float(lis[0])
        op2 = float(lis[2])

    except ValueError:
        raise FormulaError("Enter a valid Operand")

    # Check if the operator is valid
    if lis[1] == "+":
        res = op1 + op2
    elif lis[1] == "-":
        res = op1 - op2
    else:
        raise FormulaError("Enter a valid Operator")

    # Print the error
    print(opr, "=", res)
