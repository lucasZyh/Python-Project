class Student(object):
    def __init__(self, name, gender, tel, age,scores):
        self.name = name
        self.gender = gender
        self.tel = tel
        self.age = age
        self.scores = scores

        self.all_score = ""

    def __str__(self):
        return f'{self.name}, {self.gender}, {self.tel}, {self.age},{self.scores},{self.all_score}'
