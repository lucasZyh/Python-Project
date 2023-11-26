class Student(object):
    def __init__(self, name, gender, tel, age):
        self.name = name
        self.gender = gender
        self.tel = tel
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.gender}, {self.tel}, {self.age}'
