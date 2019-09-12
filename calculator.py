print("Welcome to Ancient Calculator")


def add(num1, num2):
    result = num1 + num2
    return result


def sub(num1, num2):
    result = num1 - num2
    return result


def mul(num1, num2):
    result = num1 * num2
    return result


def div(num1, num2):
    result = num1 / num2
    return result


while 1 == 1:
    choice = int(input("Options\n 1)Add \n 2)Sub \n 3)Mul \n 4)Div \n 5)Mul \n 6)Exit \n:"))
    if choice == 1:
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        print(add(x, y))
    if choice == 6:
        break
