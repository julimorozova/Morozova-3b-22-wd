import random
arr_len = 10
arr = [random.randint(1, 100 + 1) for _ in range(arr_len)]

max_element = max(arr)
min_element = min(arr)

print(f"Максимальное число в массиве: {max_element}")
print(f"Минимальное число в массиве: {min_element}")