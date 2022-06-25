username_list = []
passwords_list = []

def username_registration():
    username = input("Create Username: ")
    return username

def password_registration():
    password_valid = False
    while password_valid is False:
        password = input("Create password: ")
        password_confirmed = input("Confirm password: ")
        if password == password_confirmed:
            password_valid = True
            return password
        else:
            print("Password didn't match. Try again")

def username_validation():
    username_input = input("Enter Username: ")
    index = 0
    for element in username_list:
        if username_input == username_list[index]:
            return index
        else:
            index += 1

def password_validation(username_index):
    password_input = input("Enter password: ")
    index = 0
    for element in passwords_list:
        if password_input == passwords_list[index]:
            return index
        else:
            index += 1
            

# ----------------------------------Creating Account----------------------------------------------------
is_account_created = False
while is_account_created is False:
    username = username_registration()
    username_list.append(username)
    password = password_registration()
    passwords_list.append(password)
    break
# ----------------------------------Login Section--------------------------------------------------------
is_user_validated = False
while is_user_validated is False:
    username_index = username_validation()
    username_password_index = password_validation(username_index)
    if username_index == username_password_index:
        is_user_validated = True
        print(f"User validated! Welcome, {username}!")
    else:
        print("Wrong credentials! Try again")
        continue
# -----------------------------------Main Menu------------------------------------------------------------
