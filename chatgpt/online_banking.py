import re

class InputValidationError(Exception):
    """Custom exception for input validation errors."""
    pass

class BankAccount:
    def __init__(self, account_id: str, owner: str, balance: float = 0.0):
        # Validate account_id and owner for excessive length or improper characters
        if not re.match(r'^[a-zA-Z0-9]{1,20}$', account_id):
            raise InputValidationError(f"Invalid account ID '{account_id}'")
        if len(owner) > 50:
            raise InputValidationError(f"Owner name '{owner}' is too long")
        
        self.account_id = account_id
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount: float):
        """Deposit money into the account."""
        if amount <= 0:
            raise InputValidationError("Deposit amount must be positive.")
        
        self.balance += amount
        self.transactions.append(f"Deposit: {amount}")
    
    def withdraw(self, amount: float):
        """Withdraw money from the account if sufficient funds are available."""
        if amount <= 0:
            raise InputValidationError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InputValidationError("Insufficient balance.")
        
        self.balance -= amount
        self.transactions.append(f"Withdrawal: {amount}")
    
    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account {self.account_id}, Owner: {self.owner}, Balance: {self.balance}"

class Transaction:
    """Handles transactions like deposit, withdrawal, and transfers."""
    
    @staticmethod
    def transfer(from_account: BankAccount, to_account: BankAccount, amount: float):
        """Transfer money from one account to another, with validation."""
        if amount <= 0:
            raise InputValidationError("Transfer amount must be positive.")
        if from_account.get_balance() < amount:
            raise InputValidationError("Insufficient balance in source account.")
        
        from_account.withdraw(amount)
        to_account.deposit(amount)
        return f"Transfer of {amount} from {from_account.account_id} to {to_account.account_id} completed."

class BankSystem:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_id: str, owner: str, initial_deposit: float = 0.0):
        """Create a new bank account with input validation."""
        if initial_deposit < 0:
            raise InputValidationError("Initial deposit cannot be negative.")
        if account_id in self.accounts:
            raise InputValidationError(f"Account ID '{account_id}' already exists.")
        
        new_account = BankAccount(account_id, owner, initial_deposit)
        self.accounts[account_id] = new_account
        return new_account
    
    def get_account(self, account_id: str):
        """Retrieve an account by its ID."""
        if account_id not in self.accounts:
            raise InputValidationError(f"Account '{account_id}' does not exist.")
        return self.accounts[account_id]
    
    def transfer(self, from_account_id: str, to_account_id: str, amount: float):
        """Facilitate transfer between two accounts."""
        from_account = self.get_account(from_account_id)
        to_account = self.get_account(to_account_id)
        return Transaction.transfer(from_account, to_account, amount)
    
    def list_accounts(self):
        """List all accounts in the system."""
        return [str(account) for account in self.accounts.values()]


# Testing the system for invalid inputs and errors.
def test_improper_inputs():
    bank = BankSystem()

    try:
        # Test excessively long account ID
        bank.create_account("a" * 30, "Alice", 1000)
    except InputValidationError as e:
        print(e)  # Expect an error message

    try:
        # Test malformed account ID with special characters
        bank.create_account("Acc!123", "Alice", 500)
    except InputValidationError as e:
        print(e)  # Expect an error message

    try:
        # Test negative initial deposit
        bank.create_account("Acc123", "Alice", -500)
    except InputValidationError as e:
        print(e)  # Expect an error message

    # Create valid accounts
    alice = bank.create_account("Acc123", "Alice", 1000)
    bob = bank.create_account("Acc456", "Bob", 500)

    try:
        # Test excessive withdrawal
        alice.withdraw(5000)
    except InputValidationError as e:
        print(e)  # Expect an error message

    try:
        # Test negative transfer amount
        bank.transfer("Acc123", "Acc456", -100)
    except InputValidationError as e:
        print(e)  # Expect an error message

    try:
        # Test transfer with insufficient funds
        bank.transfer("Acc456", "Acc123", 10000)
    except InputValidationError as e:
        print(e)  # Expect an error message

    # Test valid transfer
    result = bank.transfer("Acc123", "Acc456", 200)
    print(result)  # Expect success message

    # List accounts and their balances
    print("\n".join(bank.list_accounts()))


# Run the test for improper inputs
test_improper_inputs()
