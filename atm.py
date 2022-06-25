username_list = []
passwords_list = []

def username_registration():
    username = input("Create Username: ")
    return username

def username_change(is_user_validated):
    is_change_username = True
    while is_change_username is True:
        username_change = input("Enter new Username: ")
        if username == username_change:                         # Need to be fixed! Change Username!
            print("Choose different Username.")
        else:
            username_list.remove(username)
            username = username_change
            username_list.append(username)
            print(username_list)

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

def main_menu(is_user_validated):
    while is_user_validated is True:
        print(f"1  Change Username." + "                " + "Balance  4")
        print(f"2  Change Password." + "                " + "Deposit  5")
        print(f"3  Logout." + "                        " + "Withdraw  4")
        option_input = int(input("Select an option: "))
        break
    return option_input
    
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
        break
    else:
        print("Wrong credentials! Try again")
        continue
# -----------------------------------Main Menu------------------------------------------------------------
option_selected = main_menu(is_user_validated)
while is_user_validated is True:
    if option_selected == 1:
        username = username_change(username)
        break
