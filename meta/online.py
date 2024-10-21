import re
import getpass

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


class OnlineBankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_number = input("Enter account number: ")
        account_holder = input("Enter account holder's name: ")
        if self.validate_input(account_number, account_holder):
            self.accounts[account_number] = BankAccount(account_number, account_holder)
            print("Account created successfully.")
        else:
            print("Invalid input. Please try again.")

    def login(self):
        account_number = input("Enter account number: ")
        if account_number in self.accounts:
            password = getpass.getpass("Enter password: ")
            # Assuming password is hardcoded for simplicity
            if password == "password123":
                return self.accounts[account_number]
            else:
                print("Invalid password.")
        else:
            print("Account not found.")
        return None

    def validate_input(self, account_number, account_holder):
        # Input validation rules
        if not re.match("^[0-9]{10}$", account_number):
            print("Invalid account number. Please use 10 digits.")
            return False
        if not re.match("^[a-zA-Z ]+$", account_holder):
            print("Invalid account holder's name. Please use alphabets and spaces.")
            return False
        if len(account_holder) > 50:
            print("Account holder's name is too long. Please use 50 characters or less.")
            return False
        return True


def main():
    banking_system = OnlineBankingSystem()

    while True:
        print("\n1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            banking_system.create_account()
        elif choice == "2":
            account = banking_system.login()
            if account:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Display Account Details")
                    print("4. Logout")
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        amount = float(input("Enter deposit amount: "))
                        account.deposit(amount)
                    elif choice == "2":
                        amount = float(input("Enter withdrawal amount: "))
                        account.withdraw(amount)
                    elif choice == "3":
                        account.display_details()
                    elif choice == "4":
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()