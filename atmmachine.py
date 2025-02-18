balance = 1000.00  # Set an initial balance

def display_menu():
    print("\nWelcome to the ATM!")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def check_balance():
    print(f"Your current balance is: ${balance:.2f}")

def deposit():
    global balance  # Use global variable to update balance
    try:
        amount = float(input("Enter deposit amount: $"))
        if amount > 0:
            balance += amount
            print(f"Deposit successful! Your new balance is: ${balance:.2f}")
        else:
            print("Please enter a valid amount.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def withdraw():
    global balance  # Use global variable to update balance
    try:
        amount = float(input("Enter withdrawal amount: $"))
        if amount > 0:
            if amount <= balance:
                balance -= amount
                print(f"Withdrawal successful! Your new balance is: ${balance:.2f}")
            else:
                print("Insufficient balance!")
        else:
            print("Please enter a valid amount.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def atm_machine():
    while True:
        display_menu()
        choice = input("Please select an option (1-4): ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the ATM machine program
atm_machine()