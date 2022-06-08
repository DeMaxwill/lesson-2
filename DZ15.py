def arithmetic(arg1, arg2, operations):

    operators = {"+": lambda num1, num2: num1 + num2,
                 "-": lambda num1, num2: num1 - num2,
                 "*": lambda num1, num2: num1 * num2,
                 "/": lambda num1, num2: num1 / num2,
                 }

    if operations not in operators:
        return "!Неизвестная Операция!"
    else:
        return operators.get(operations)(arg1, arg2)

result = arithmetic(7, 8, "&")
print(result)
