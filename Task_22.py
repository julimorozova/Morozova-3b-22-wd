import random
arr_len = 10
arr = [random.randint(1, 10 + 1) for _ in range(arr_len)]
sum_elements = 0
for el in arr:
    sum_elements += el
print(f"Сумма элементов в массиве {arr} равна {sum_elements}")