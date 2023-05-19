class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.age = age
        self.breed = breed

    def get_info(self):
        return f"Имя: {self.name}\nПорода: {self.breed}\nВозраст: {self.age}"


dog = Dog('Рекс','Шпиц', 2)
print(dog.get_info())