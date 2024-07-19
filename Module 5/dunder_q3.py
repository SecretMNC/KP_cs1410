class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar.x, self.y * scalar.y)
    
    def __str__(self):
        return f'<{self.x},{self.y}>'
        
v1 = Vector(1, 2)
v2 = Vector(2, 3)

result_add = v1 + v2
result_sub = v1 - v2
result_mul = v1 * v2

print(result_add)
print(result_sub)
print(result_mul)
# Could not figure out the formatting, but the numbers are correction