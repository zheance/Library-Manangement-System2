import functions
users = {'Mayank':'password'}

def passwordreq(password):
    if len(password) < 8:
        return "Password should be at least 8 characters long"
    else:
        return False

def signup():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users:
        print("User already exists")
    else:
        password_error = passwordreq(password)
        if password_error is False:
            users[username] = password
            print("Signup successful")
        else:
            print(password_error)
#Hello THere
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users:
        if users[username] == password:
            print("Login successful")
            functions.mainpy()
            
        else:
            print("Incorrect password")
    else:
        print("User does not exist")

while True:
    print("1. Signup\n2. Login\n3. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        signup()
    elif choice == 2:
        login()
    elif choice == 3:
        print("Exiting the Program....:")
        break
    else:
        print("Invalid choice")
