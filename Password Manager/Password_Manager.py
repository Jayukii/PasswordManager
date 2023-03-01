import getpass
import json

PASSWORDS_FILE = 'passwords.json'

def load_passwords():
    try:
        with open(PASSWORDS_FILE, 'r') as f:
            passwords = json.load(f)
    except FileNotFoundError:
        passwords = {}
    return passwords

def save_passwords(passwords):
    with open(PASSWORDS_FILE, 'w') as f:
        json.dump(passwords, f)

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

def set_password(account, password):
    passwords = load_passwords()
    passwords[account] = password
    save_passwords(passwords)

def delete_password(account):
    passwords = load_passwords()
    if account in passwords:
        del passwords[account]
        save_passwords(passwords)
        print(f"Deleted password for {account}")
    else:
        print(f"No password found for {account}")

def list_accounts():
    passwords = load_passwords()
    print("Account with stored password:")
    for account in passwords:
        print(account)

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



