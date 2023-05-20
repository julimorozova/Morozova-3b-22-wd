class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def presentation(self):
        print(f"Имя: {self.name}.\nВозраст: {self.age} лет.\nЗарплата: {self.salary} руб.")


employee = Employee('Ivan Ivanov', 26, 12000)
employee.presentation()