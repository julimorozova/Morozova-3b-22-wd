def is_prime(number):
    divider = 2
    while number % divider != 0:
        divider += 1
    return divider == number

print(is_prime(5))
print(is_prime(4))