import getpass
import json
#using the getpass module to securely prompt the user for their password without displaying it on the screen
#json module to store the account information in a JSON file
PASSWORDS_FILE = 'passwords.json'

#load_passwords() function loads the account information from the JSON file
def load_passwords():
    try:
        with open(PASSWORDS_FILE, 'r') as f:
            passwords = json.load(f)
    except FileNotFoundError:
        passwords = {}
    return passwords

#save_passwords() function saves the account information to the JSON file
def save_passwords(passwords):
    with open(PASSWORDS_FILE, 'w') as f:
        json.dump(passwords, f)

#get_password() function prompts the user for their password and checks if it matches the stored password for the given account
def get_password(account):
    passwords = load_passwords()
    if account in passwords:
        password = get_password(f"Enter password for {account}: ")
        if password == passwords[account]:
            print(f"Password for {account}: {passwords[account]}")
        else:
            print("Incorrect password")
    else:
        print(f"No password found for {account}")

#set_password() function sets the password for the given account
def set_password(account, password):
    passwords = load_passwords()
    passwords[account] = password
    save_passwords(passwords)

#delete_password() function deletes the stored password for the given account
def delete_password(account):
    passwords = load_passwords()
    if account in passwords:
        del passwords[account]
        save_passwords(passwords)
        print(f"Deleted password for {account}")
    else:
        print(f"No password found for {account}")

#list_accounts() function lists all the accounts for which passwords are stored
def list_accounts():
    passwords = load_passwords()
    print("Account with stored password:")
    for account in passwords:
        print(account)

#main() function provides a menu for the user to select the desired option
def main():
    while True:
        print("\n0ptions:")
        print("1. Get password")
        print("2. Set password")
        print("3. Delete password")
        print("4. List accounts")
        print("5. Quit")
        choice = input("Enter choice: ")
        if choice == '1':
            account = input("Enter Account: ")
        elif choice == '2':
            account = input("Enter account: ")
            password = getpass.getpass("Enter password: ")
            set_password(account, password)
        elif choice == '3':
            account = input("Enter account: ")
            delete_password(account)
        elif choice == '4':
            list_accounts()
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()



