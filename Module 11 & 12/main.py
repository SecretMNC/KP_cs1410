from user import *
from sqlalchemy.orm import sessionmaker


def add_user(session, name, age, email):
    
    new_user = User(name=name, age=age, email=email)
    session.add(new_user)
    session.commit()
    print(f'User: {name} has been added successfully.')


def read_user(session):
    users = session.query(User).all()
    print(f'Display all users:')
    for user in users:
        print(user.id, user.name, user.age, user.email)


def find_user_by_age(session, age):
    older_users = session.query(User).filter(User.age > age).all()
    print(f'Users older than {age}:')
    for user in older_users:
        print(user.id, user.name, user.age, user.email)


def delete_user(session, user_id):
    del_user = session.get(User, user_id)
    if del_user:    
        session.delete(del_user)
        session.commit()
        print(f'info: userID {user_id} has been removed.')
    else:
        print(f'error: userID {user_id} does ot exist.')

     

def main():
    # Create a session factory
    Session = sessionmaker(bind=engine)
    session = Session()
    add_user(session,'John Doe',30, 'john.doe@example.com')
    read_user(session)
    find_user_by_age(session, 25)

    delete_user(session, 1)
    session.close()


if __name__== '__main__':
    main()