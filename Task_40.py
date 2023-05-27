import os


def has_file(dir_name, file_name):
    files = os.listdir(dir_name)
    result = "Файла не существует"

    for file in files:
        if file == file_name:
            result = "Файл существует"
            break

    print(result)


has_file('.', 'text.txt')
