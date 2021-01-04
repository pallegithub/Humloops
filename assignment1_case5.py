#Login app
print('Enter correct Username and Password to continue')
attempt=0
while attempt < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='Username' and username=='Password':
        print("Login Succesfully")
        break
    else:
        print('wrrong Credtessentials')
        attempt = attempt + 1