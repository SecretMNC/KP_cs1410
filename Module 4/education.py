class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

class Course:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Student(User):
    def __init__(self, first_name, last_name, role):
        super().__init__(first_name, last_name)
        self.role = role

class Instructor(User):
    def __init__(self, role):
        self.role = role


class Assessment:
    pass

class QuizAssessment(Assessment, Quiz):
    pass