USER_DATA_FILE = "user_data.txt"

def load_user_data():
    try:
        with open(USER_DATA_FILE, 'r') as file:
            return [line.strip().split(':') for line in file]
    except FileNotFoundError:
        return []

def save_user_data(users):
    with open(USER_DATA_FILE, 'w') as file:
        for username, password in users:
            file.write(f"{username}:{password}\n")

def register(users):
    print("=== Register ===")
    username = input("Enter username: ")
    
    if any(user[0] == username for user in users):
        print("Username already exists. Please choose another username.")
        return
    
    password = input("Enter password: ")
    users.append((username, password))
    save_user_data(users)
    print("Registration successful!")

def login(users):
    print("=== Login ===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if any(user[0] == username and user[1] == password for user in users):
        print("Login successful!")
    else:
        print("Login failed. Please check your username and password.")

def main():
    users = load_user_data()

    while True:
        print("\n=== User Login System ===")
        print("1. Register")
        print("2. Login")
        print("3. Change Password")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            register(users)
        elif choice == '2':
            login(users)
        elif choice == '3':
            change_password(users)
        elif choice == '4':
            save_user_data(users)
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

main()
