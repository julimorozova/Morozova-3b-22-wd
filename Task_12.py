class Student:
    def __init__(self, fist_name, last_name, course, grades):
        self.fist_name = fist_name
        self.last_name = last_name
        self.course = course
        self.grades = grades

    def get_average_mark(self):
        result = round(sum(self.grades) / len(self.grades), 2)
        return f"Средний бал студента {self.fist_name} {self.last_name} {self.course} курса равен {result}"


student = Student('Иван', 'Иванов', '5', [4,5,3,4,5,4,5,5,5,3,3,4,5,4])
print(student.get_average_mark())