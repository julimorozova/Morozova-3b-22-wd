def calculate_least_common_multiple(num1, num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2

    while True:
        if (greater % num1 == 0) and (greater % num2 == 0):
            lcm = greater
            break
        greater += 1
    return lcm


num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

print(f"Наименьшее общее коатное для чисел равно {calculate_least_common_multiple(num1, num2)}")
