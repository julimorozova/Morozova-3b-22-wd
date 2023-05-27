try:
    num = int(input('Введите число: '))
    result = num * num
    print(f'Квадрат числа {num} равен {result}')
except Exception:
    print('Ошибка')
finally:
    print('\nЗавершение программы')