import getpass
import hashlib
import uuid


class Account:
    def __init__(self, account_number, username, password, balance=0):
        self.account_number = account_number
        self.username = username
        self.password = self._hash_password(password)
        self.balance = balance

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.password == self._hash_password(password)

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit Successful. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawal Successful. New balance: ${self.balance}")


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, username, password):
        account_number = str(uuid.uuid4().int)
        self.accounts[account_number] = Account(account_number, username, password)
        print(f"Account created successfully. Account Number: {account_number}")

    def login(self, account_number, password):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            if account.check_password(password):
                return account
            else:
                print("Incorrect password.")
        else:
            print("Account not found.")
        return None

    def display_balance(self, account):
        print(f"Account Balance: ${account.balance}")


def main():
    bank = BankSystem()

    while True:
        print("\n1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            bank.create_account(username, password)
        elif choice == "2":
            account_number = input("Enter account number: ")
            password = getpass.getpass("Enter password: ")
            account = bank.login(account_number, password)
            if account:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")
                    choice = input("Choose an option: ")

                    if choice == "1":
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                    elif choice == "2":
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                    elif choice == "3":
                        bank.display_balance(account)
                    elif choice == "4":
                        break
                    else:
                        print("Invalid option.")
        elif choice == "3":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
