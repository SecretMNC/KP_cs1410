def new_credential():
    with open('credentials.txt', 'w') as creds:
        username = input('Please type in a username\n')
        password = input('Please type in a password\n')
        creds.write(f'{username}\n')
        creds.write(f'{password}\n')
        
def check_cred():
    username = input('What is your username?\n')
    password = input('What is your password?\n')
    with open('credentials.txt', 'r') as creds:
        lines = creds.read().splitlines()
        lst = []
        for line in lines:
            lst.append(line)
            
        print(lst)
    if lst[0] == username and lst[1] == password:
        return 'You are now logged in!'
    else:
        return 'Login unsuccessful. Please try again.'

new_credential()
print(check_cred())