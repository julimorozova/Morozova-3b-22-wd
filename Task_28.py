def calculator(num1, num2, operation):
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        print(num1 / num2)
    else:
        print("Некорректная операция")

calculator(1, 5, "+")
calculator(11, 5, "-")
calculator(1, 5, "f")
