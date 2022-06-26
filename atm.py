username_list = []
passwords_list = []

def atm_run():
    print("1. Create Account")
    print("2. Login")
    first_menu_input = int(input("Hello! Welcome to ATM! Please, select option: "))
    return first_menu_input

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
            print(f"Your new Username is {username_change}")
            break

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

def password_change(is_user_validated):
    is_change_password = True
    while is_change_password is True:
        password_change = input("Enter new Password: ")
        if password == password_change:                         # Need to be fixed! Change Username!
            print("Old password entered")
        else:
            new_password = input("Confirm new password: ")
            if new_password == password_change:
                print(f"Your new password is {new_password}")
                break

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
        print(f"1  Change Username" + "                " + "Balance  4")
        print(f"2  Change Password" + "                " + "Deposit  5")
        print(f"3  Logout" + "                        " + "Withdraw  6")
        option_input = int(input("Select an option: "))
        break
    return option_input

def check_balance(balance):
    if balance <= float(0):
        print(f"Your current balance is ${balance}")
    else:
        print(f"Your current balance is ${balance}")

def deposit():
    deposit_amount = float(input("How much would you like to deposit?: $"))
    return deposit_amount

def withdraw(balance):
    withdraw = True
    while withdraw is True:
        withdraw_amount = float(input("How much would you like us to dispend?: $"))
        if withdraw_amount > balance and balance == float(0):
            print(f"Sorry, your balance is ${balance}. We can't proceed this operation.")
        elif withdraw_amount > balance:
            print(f"You can't withdraw ${withdraw_amount}, because your balance is ${balance}")
        else:
            new_balance = float(balance) - float(withdraw_amount)
            print(f"After this withdraw your current balance is ${new_balance}")
            return float(new_balance)

# ----------------------------------ATM Start ----------------------------------------------------------
app_start = True
while app_start is True:
    first_menu_input = atm_run()
    if first_menu_input == 1:
        is_account_created = False
    elif first_menu_input == 2:
        username_input = input("Enter Username: ")
        print(f"Account with name {username_input} does not exist!")
        continue
    else:
        print("Please, select correct option!")
        continue
    # ----------------------------------Creating Account----------------------------------------------------
    while is_account_created is False:
        username = username_registration()
        username_list.append(username)
        password = password_registration()
        passwords_list.append(password)
        print(f"Account created!")
        print(f"Username: {username}")
        print(f"Password: {password}")
        break
        # ----------------------------------Login Section--------------------------------------------------------
    
    is_user_validated = False
    while is_user_validated is False:
        print("Please, enter Username and Password to login.")
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
    balance = float(0)
    while is_user_validated is True:
        option_selected = main_menu(is_user_validated)
        if option_selected == 1:
            username = username_change(username)
            continue
        elif option_selected == 2:
            password = password_change(password)
            continue
        elif option_selected == 3:
            print("Thanks for using our service. Have a great day!")
            break
        elif option_selected == 4:
            check_balance(balance)
            continue
        elif option_selected == 5:
            deposit_amount = deposit()
            new_balance = float(balance) + float(deposit_amount)
            balance = new_balance
            print(f"After this deposit your balance is ${balance}")
            continue
        elif option_selected == 6:
            new_balance = withdraw(balance)
            balance = float(new_balance)
            continue
        else: 
            print("Please, select option!")
            continue