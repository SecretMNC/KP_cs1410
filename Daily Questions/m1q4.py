grades = {"Alice": 85, "Bob": 92, "Charlie": 88, "David": 94}

def highest_scorer(data):
    highest_name = ''
    highest_grade = 0
    for key, value in data.items():
        if value >= highest_grade:
            highest_name = key
            highest_grade = value
    
    return highest_name
    
print(highest_scorer(grades))
