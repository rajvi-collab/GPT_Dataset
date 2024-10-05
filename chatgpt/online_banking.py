import datetime

class Account:
    def __init__(self, account_number, name, initial_balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append((f"Deposit: {amount}", datetime.datetime.now()))
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append((f"Withdrawal: {amount}", datetime.datetime.now()))
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions

class Transaction:
    def transfer(self, sender_account, receiver_account, amount):
        if sender_account.balance >= amount and amount > 0:
            sender_account.withdraw(amount)
            receiver_account.deposit(amount)
            print(f"Transferred ${amount} from Account {sender_account.account_number} to Account {receiver_account.account_number}.")
        else:
            print("Transfer failed: Insufficient funds or invalid amount.")

class BankingSystem:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1000

    def create_account(self, name, initial_balance=0):
        account_number = self.next_account_number
        self.accounts[account_number] = Account(account_number, name, initial_balance)
        self.next_account_number += 1
        print(f"Account created for {name}. Account Number: {account_number}")
        return account_number

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def list_accounts(self):
        for acc_num, account in self.accounts.items():
            print(f"Account Number: {acc_num}, Name: {account.name}, Balance: ${account.balance}")

# Example of usage
if __name__ == "__main__":
    bank_system = BankingSystem()
    
    # Create two accounts
    acc_1 = bank_system.create_account("Alice", 1000)
    acc_2 = bank_system.create_account("Bob", 500)

    # Access the accounts
    account1 = bank_system.get_account(acc_1)
    account2 = bank_system.get_account(acc_2)
    
    # Perform transactions
    account1.deposit(200)
    account2.withdraw(100)
    
    # Transfer money
    transaction_manager = Transaction()
    transaction_manager.transfer(account1, account2, 300)
    
    # List accounts and their balances
    bank_system.list_accounts()
    
    # View transaction history
    print("\nAlice's Transaction History:")
    for transaction in account1.get_transaction_history():
        print(transaction)

    print("\nBob's Transaction History:")
    for transaction in account2.get_transaction_history():
        print(transaction)
