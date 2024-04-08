"""
    ATM.py
"""

class ATM:
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.transactions = []

    def deposit(self, account, amount):
        account.current_balance = account.current_balance + amount
        self.transactions.append(f"Deposit: ${amount} to Account {account.account_number}")
        print("Deposit Complete")

    def withdraw(self, account, amount):
        account.current_balance = account.current_balance - amount
        self.transactions.append(f"Withdraw: ${amount} from Account {account.account_number}")
        print("Withdraw Complete")

    def check_currentbalance(self, account):
        print(account.current_balance)

    def view_transaction_summary(self):
        print("Transaction Summary:")
        for transaction in self.transactions:
            print(transaction)