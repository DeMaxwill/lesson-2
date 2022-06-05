a_dict = '2', '4', '6', '8'
b_dict = '3', '5', '7', '9'
c_dict = '+', '-', '*', '/'

a=a_dict
b=b_dict
c=c_dict


def arithmetic(a, b, c):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        return a / b
    else:
        print("Неизвестная операция ")

arithmetic(a, b, c)
