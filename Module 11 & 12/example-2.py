# SQLAlchemy Classes for Students and Classes

# In this example, we define SQLAlchemy classes to represent students and classes 
# in a school management system. The classes are designed without explicit 
# relationships to keep the schema simple and straightforward.

# Student Class:
# - The `Student` class represents individual students in the system.
# - Attributes:
#   - `id`: Primary key identifying the student.
#   - `name`: Name of the student.
#   - `age`: Age of the student.
#   - `class_id`: Foreign key referencing the class the student belongs to.

# Class Class:
# - The `Class` class represents individual classes offered by the school.
# - Attributes:
#   - `id`: Primary key identifying the class.
#   - `name`: Name of the class.
#   - `teacher`: Name of the teacher or instructor teaching the class.

# Database Schema:
# - The schema consists of two tables: `students` and `classes`.
# - The `students` table stores information about each student, including their name, age, 
#   and the class they belong to identified by `class_id`.
# - The `classes` table stores information about each class, including the class name and
#   the teacher assigned to teach that class.

# Relationship Handling:
# - Instead of using explicit relationships, the `Student` class manages class associations 
#   through a direct foreign key reference (`class_id`).
# - This design simplifies the schema by avoiding the need for complex relationship mappings,
#   suitable for scenarios where direct associations are sufficient.

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    class_id = Column(Integer)

class Class(Base):
    __tablename__ = 'classes'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher = Column(String)

engine = create_engine('sqlite:///student.db')
Base.metadata.create_all(engine)