class Student:
    def __init__(self, fist_name, last_name, age, speciality):
        self.fist_name = fist_name
        self.last_name = last_name
        self.age = age
        self.speciality = speciality

    def get_info(self):
        print(f"Карточка студента:\nИмя: {self.fist_name} {self.last_name}.\nВозраст: {self.age}.\nСпециальность: {self.speciality}.")


student = Student('Иван', 'Иванов', 23, 'Software developer')
student.get_info()