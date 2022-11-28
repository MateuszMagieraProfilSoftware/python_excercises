print("1. Write a program that serves as a basic calculator. It asks for two numbers, then it asks\
for an operator. Gracefully deal with input that doesn’t cleanly convert to numbers.\
Deal with division by zero errors.")


def calculator(num1,num2,operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == "/":
        try:
            num1 / num2
        except ZeroDivisionError:
            print("Don't you dare dividing by zero!!!")
        return num1 / num2


print(calculator(1000000000000,5,"*"))


