class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Имя: {self.name}\nВозраст: {self.age}"


person = Person('Игорь', 34)
print(person.get_info())