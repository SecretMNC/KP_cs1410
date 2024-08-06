from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

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

def add_student(session, id, name, age, class_id):
    new_user = Student(id=id, name=name, age=age, class_id=class_id)
    session.add(new_user)
    session.commit()
    print(f'Student: {name} has been added successfully.')

def add_class(session, id, name, teacher):
    new_user = Student(id=id, name=name, teacher=teacher)
    session.add(new_user)
    session.commit()
    print(f'Class: {name} has been added successfully.')

def display_students(session):
    students = session.query(Student).all()
    print(f'Display all students:')
    for student in students:
        print(student.id, student.name, student.age, student.class_id)

def display_classes(session):
    classes = session.query(Class).all()
    print(f'Display all students:')
    for class_ in classes:
        print(class_.id, class_.name, class_.teacher)

engine = create_engine('sqlite:///student.db')
Base.metadata.create_all(engine)


def main():
    try:
        Session = sessionmaker(bind=engine)
        session = Session()

        add_student(session, 1313, 'John Doe', 30, 1)
        display_students(session)

        add_class(session, 1, "CS101", "Jane Doe")
        display_classes(session)
    except (Exception, AttributeError) as err:
        print(err)
    finally:
        session.close()

if __name__ == "__main__":
    main()
