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
    print("1)ADDITON 2)SUBTRACTION 3)MULTIPLICATION 4)DIVISION 5)EXIT")
    choice = int(input("Please enter your choice:"))

    if choice == 1:
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        print(add(n1, n2))
    elif choice == 2:
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        print(sub(n1, n2))
    elif choice == 3:
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        print(mul(n1, n2))
    elif choice == 4:
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        print(div(n1, n2))
    elif choice == 5:
        break
    else:
        print("Sorry invalid choice,please give an valid choice")
