import getpass

def login():
    password = 'naruto'

    print("Welcome to the Login System")
    print("1. Password visibility")
    print("2. Access")
    print("3. Instant Verification")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Enter password (visibility is hidden):")
            entered_password = getpass.getpass()
            print("Password entered:", '*' * len(entered_password))
        
        elif choice == "2":
            print("Enter password:")
            entered_password = input()
            if entered_password == password:
                print("Access granted! You are now logged in.")
                break
            else:
                print("Wrong password. Please try again.")

        elif choice == "3":
            print("Enter password for instant verification:")
            entered_password = input()
            if entered_password == password:
                print("Instant verification successful! You are now logged in.")
                break
            else:
                print("Wrong password. Please try again.")

        else:
            print("Invalid choice. Please enter a valid option.")

login()
