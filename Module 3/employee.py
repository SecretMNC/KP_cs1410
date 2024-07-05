class Employee:
    
    raise_perc = 1.04
    
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        
    def get_fullname(self):
        return f'--> {self.first_name} {self.last_name}'
    
    def greetings(self):
        return f"--> Hello"

class Developer(Employee):
    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
        self.prog_lang = prog_lang
        
    def say_hello(self):
        return f"hello {self.first_name}"
    
    def greetings(self):
        return f"--> Bonjour"

class Manager(Employee):
    def __init__(self, first_name, last_name, pay, level, employees=None):
        super().__init__(first_name, last_name, pay)
        self.level = level
        self.employees = []
        
    def add_emp(self, name):
        self.employees.append(name)
    
    def rm_emp(self, name):
        if name.first_name in self.employees:
            self.employees.remove(name)
        else:
            print(f'{name.first_name} {name.last_name} is already not your employee.')
            
    def greetings_from_manager(self):
        return f"--> Howdy"
        
    @staticmethod
    def display_emp(name):
        return f'''First name: {name.first_name}
Last name: {name.last_name}
Salary: {name.pay}'''

man_1 = Manager('Susan', 'Larson', 40000, 'level-3')
dev_1 = Developer('Bob', 'Clark', 80000, 'Python')
print(man_1.greetings_from_manager())
print(man_1.greetings())
print(dev_1.greetings())


# print(man_1.first_name, man_1.last_name, man_1.pay, man_1.level)
# print(dev_1.first_name, dev_1.last_name, dev_1.pay, dev_1.prog_lang)

#print(man_1.display_emp(dev_1))

