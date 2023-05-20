import random
arr_len = 10
arr = [random.randint(1, 100 + 1) for _ in range(arr_len)]

while True:
    num = int(input('Введите число от 1 до 100 или введите 0, чтобы завершить игру: '))
    if num == 0:
        break

    count_num = arr.count(num)
    if count_num > 0:
        print('Число найдено в массиве')
    else:
        print('Число не найдено в массиве')