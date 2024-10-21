import random
import string

class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def check_balance(self):
        return self.balance

def validate_pin(pin):
    return len(pin) == 4 and all(c.isdigit() for c in pin)

def validate_amount(amount):
    try:
        amount = float(amount)
        return amount > 0
    except ValueError:
        return False

class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_number = ''.join(random.choices(string.digits, k=10))
        pin = input("Enter a 4-digit PIN: ")
        while not validate_pin(pin):
            print("Invalid PIN. Please enter a 4-digit number.")
            pin = input("Enter a 4-digit PIN: ")
        self.accounts[account_number] = Account(account_number, pin)
        print("Account created successfully. Your account number is:", account_number)

    def login(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")
        if account_number in self.accounts and self.accounts[account_number].pin == pin:
            return account_number
        else:
            print("Invalid account number or PIN.")
            return None

    def deposit(self, account_number):
        amount = input("Enter the amount to deposit: ")
        if validate_amount(amount):
            if self.accounts[account_number].deposit(float(amount)):
                print("Deposit successful.")
            else:
                print("Invalid amount.")
        else:
            print("Invalid amount.")

    def withdraw(self, account_number):
        amount = input("Enter the amount to withdraw: ")
        if validate_amount(amount):
            if self.accounts[account_number].withdraw(float(amount)):
                print("Withdrawal successful.")
            else:
                print("Insufficient funds or invalid amount.")
        else:
            print("Invalid amount.")

    def check_balance(self, account_number):
        print("Your current balance is:", self.accounts[account_number].check_balance())

def main():
    banking_system = BankingSystem()
    while True:
        print("\nChoose an option:")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            banking_system.create_account()
        elif choice == '2':
            account_number = banking_system.login()
            if account_number:
                while True:
                    print("\nChoose an option:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")
                    choice = input("Enter your choice: ")

                    if choice == '1':
                        banking_system.deposit(account_number)
                    elif choice == '2':
                        banking_system.withdraw(account_number)
                    elif choice == '3':
                        banking_system.check_balance(account_number)
                    elif choice == '4':
                        break
                    else:
                        print("Invalid choice.")
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()