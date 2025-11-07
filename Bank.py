class BankAccount:
    def __init__(self, account_number, name, account_type, balance=0.0):
        """Initialize the bank account details."""
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            print(f"Deposited ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")

    def withdraw(self, amount):
        """Withdraw money from the account if balance is sufficient."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance! Transaction failed.")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount:.2f}. Remaining balance: ₹{self.balance:.2f}")

    def display_account(self):
        """Display account details."""
        print("\nAccount Details:")
        print(f"Account Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: ₹{self.balance:.2f}")


# Example usage
account1 = BankAccount("123456", "Alice", "Savings", 5000)

account1.display_account()
account1.deposit(1500)
account1.withdraw(2000)
account1.withdraw(6000)  # Example of insufficient funds
account1.display_account()
