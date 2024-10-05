class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def check_balance(self):
        print(f"Account balance: ${self.balance}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, name)
            print(f"Account created for {name}.")
        else:
            print("Account number already exists.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

# Example usage
bank = Bank()
bank.create_account("123456", "Alice")
account = bank.get_account("123456")
if account:
    account.deposit(1000)
    account.withdraw(500)
    account.check_balance()
