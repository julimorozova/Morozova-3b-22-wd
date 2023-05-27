try:
    file = open('test.txt', 'w')
    file.write('Hello, world!')
    file.close()
except Exception:
    print('Ошибка')
finally:
    print('\nЗавершение программы')