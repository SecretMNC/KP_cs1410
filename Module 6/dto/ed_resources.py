# Content Classes
class Quiz:
    def __init__(self, name, q_list):
        self.name = name
        self.q_list = q_list
        
class Course:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        
    def display_course(self):
        return f'''Course name: {self.name}
Duration of course: {self.duration}'''
    
# User Classes
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role
        
    def display_user(self):
        return f'''Username: {username}
User's role: {role}'''
    
class Student(User):
    pass

class Intructor(User):
    def __init__(self, students=None):
        if students == None:
            self.students = []
        elif len(self.students) == 0:
            self.students = students
        else:
            self.students.append = students

class Admin(User):
    def change_user(self, user, new_username, new_role):
        if isinstance(new_username, str) and isinstance(new_role, str):
            user.username = new_username
            user.new_role = new_role
        
        

#Assessment Classes
class Assessment:
    def __init__(self, name, points):
        self.name = name
        self.points = points
        
    def display_assessment(self):
        return f'''Assessment name: {self.name}
Total points: {self.points}'''
    
class QuizAssessment(Assessment, Quiz):
    def __init__(self):
        pass