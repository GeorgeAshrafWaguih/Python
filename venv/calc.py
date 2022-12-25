on = True


def add():
    a = float(input("Enter number a : "))
    b = float(input("Enter number b : "))
    print(a + b)


def subtraction():
    a = float(input("Enter number a : "))
    b = float(input("Enter number b : "))
    print(a - b)


def multiply():
    a = float(input("Enter number a : "))
    b = float(input("Enter number b : "))
    print(a * b)


def divide():
    a = float(input("Enter number a : "))
    b = float(input("Enter number b : "))
    print(a / b)

while on:
    operation = input("Please type +, -, *, /, or q to exit")
    if operation == '+':
        add()
    elif operation == '-':
        subtraction()
    elif operation == '*':
        multiply()
    elif operation == '/':
        divide()
    elif operation == 'q':
        on = False
    else:
        print("THAT OPERATION IS NOT AVAILABLE")
