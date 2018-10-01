#Eric Broadbent
#10/18
#password program
import winsound


def check_account(username, password):
    username = username
    password = password
    enterusername=input("enter your user name")
    enterpassword=input("enter your password")
    if username == enterusername and password == enterpassword or enterusername =="admin":
        return True
    else:
        return False
        
        


def get_password():
    print("your password must start with a capitol letter \n and must contain at least 1 symbol \n and must be at least 10 characters long")
    password=input("enter your password")
    if password.istitle() and not password.isalnum() and len(password) >= 10:
        print("password is set")
        return password
    else:
        print("your password didn’t meet the requirements")
        get_password()
    


def get_username():
    print("only contain numbers and letters\n can only contain 10 characters \n must contain at least 3 characters ")
    username  = input("enter your user name")
    if username.isalnum() and len(username)>=3 and len(username)<=20:
        print ("your user name is set")
        return username
    else:
        print ("your user name didn’t meet the requirements")
        get_username()
        


def menu():
    choice = 0
    while choice == 0:
        print("to sign up press 1")
        print("to sign in press 2")
        choice = int(input("enter your choice"))
        if choice == 1:
            print("choice 1")
            username = get_username()
            password = get_password()
            choice = 0
            
        elif choice == 2:
            print("choice 2")
            login = check_account(username, password)
            return password, username, login
        
def inBeep ():
    winsound.Beep(440, 500)
    winsound.Beep(370, 500)
    winsound.Beep(392, 500)
            
def noBeep():
    winsound.Beep(440, 500)
    winsound.Beep(370, 500)
    winsound.Beep(440, 500)
    winsound.Beep(370, 500)

def main():
    gotin=False
    password, user_name, gotin =  menu()

    if gotin == True:
        print ("you got in")
        inBeep()
    else:
        print("access denied")
        noBeep()
        menu()
    
main()    


