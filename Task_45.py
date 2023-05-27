try:
    file_name = input('Введите имя файла: ')
    file = open(file_name, 'r')
    print(file.read())
    file.close()
except Exception:
    print('Ошибка')
finally:
    print('\nЗавершение программы')