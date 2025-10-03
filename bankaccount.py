class Bank:
    def _init_(self):
        self.name = ""
        self.account_no = ""
        self.account_type = ""
        self.balance = 0.0
    
    def assign_initial_values(self):
        # Assign initial values for the new customer
        self.name = input("Enter Your Name: ")
        self.account_no = input("Enter Account Number: ")
        self.account_type = input("Enter Account Type: ")
        self.balance = float(input("Enter Your Balance: "))
        print("Account successfully created!")

    def deposit(self):
        # Deposit amount to the account
        depo = float(input("Enter Value To Deposit: "))
        self.balance += depo
        print(f"Deposited {depo}. New balance is {self.balance}")

    def withdraw(self):
        # Withdraw amount from the account
        withd = float(input("Enter The Amount to Withdraw: "))
        if withd <= self.balance:
            self.balance -= withd
            print(f"Withdrawn {withd}. New balance is {self.balance}")
        else:
            print("Insufficient balance for this withdrawal.")

    def display(self):
        # Display account details
        print("\nAccount Details:")
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_no}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")


v = True
obj1 = Bank()

while v:
    # Display menu options
    print("\n1. New Customer")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display")
    print("5. Exit")
    
   
    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj1.assign_initial_values()
    elif choice == 2:
        obj1.deposit()
    elif choice == 3:
        obj1.withdraw()
    elif choice == 4:
        obj1.display()
    elif choice == 5:
        print("Exiting the program.")
        v = False
    else:
        print("Invalid choice. Please try again.")
        