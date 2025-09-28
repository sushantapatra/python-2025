class Atm:
    #Constructor
    def __init__(self):
        self.pinNumber = ""
        self.balance = 0
        self.menu()

    def create_pin(self):
        new_pin = int(input("Enter your new pin: "))
        self.pinNumber = new_pin
        print("Pin created successfully.")
        
    def deposit(self):
        temp_pin = int(input("Enter your pin: "))
        if temp_pin != self.pinNumber:
            print("Incorrect pin. Transaction cancelled.")
            return
        
        deposit_amount = int(input("Enter amount to deposit: "))
        self.balance += deposit_amount
        print(f"Deposited: {deposit_amount}. New balance: {self.balance}")  
        
    def withdraw(self):
        temp_pin = int(input("Enter your pin: "))
        if temp_pin != self.pinNumber:
            print("Incorrect pin. Transaction cancelled.")
            return
        
        withdraw_amount = int(input("Enter amount to withdraw: "))
        if withdraw_amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= withdraw_amount
            print(f"Withdrew: {withdraw_amount}. New balance: {self.balance}")
            
    def check_balance(self):
        temp_pin = int(input("Enter your pin: "))
        if temp_pin != self.pinNumber:
            print("Incorrect pin. Transaction cancelled.")
            return
        print(f"Your current balance is: {self.balance}")
        
    def exit(self):
        print("Thank you for using the ATM. Goodbye!")
        quit()
        
            
    def menu(self):
        user_input = input("""
            Hello! How would you like to proceed?
            1. Enter 1 to create pin
            2. Enter 2 to deposit
            3. Enter 3 to withdraw
            4. Enter 4 to check balance
            5. Enter 5 to exit          
        """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            self.exit()
        else:
            print("Invalid input. Please try again.")

        
        

sbi_atm = Atm()