def get_password():
    print("your password must start with a capitol letter \n and must contain at least 1 symbol \n and must be at least 10 characters long")
    password=input("enter your password")
    if len(password)>10 and password.istitle() and not password.isalnum():
        print("your password is set")
        
        return password
    else:
        print("your password didn’t meet the requirements")
    

def get_user_name():
    print("requirements for user name")
    user_name  = input("enter your user name")
    if user_name:
        print ("your user name is set")
    else:
        print ("your user name didn’t meet the requirements")

def menu():
    choice = 0
    print ("to sign up press 1")
    print("to sign in press 2")

    choice = int(input("enter your choice"))
    if choice == 1:
        get_user_name()
        get_password()
    if choice == 2:
        check_login()
    else:
        print("thats not an option")

   
