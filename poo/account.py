# account.py
""" Account class definition. """
from decimal import Decimal


class Account:
    """ Account class for maintaining a bank account balance """
    
    def __init__(self, name, balance):
        """ Initialize an Account object """
        
        # if balance is less than 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00')
        
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        """ Deposit money to the account. """
        
        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive')
        
        self.balance += amount
        
    def withdrawal(self, amount):
        if amount > self.balance:
            raise ValueError('amount must be <= to balance')
        elif amount < Decimal('0.00'):
            raise ValueError('amount must be positive')
        
        self.balance -= amount
        
    def __str__(self):
        return f"Name: {self.name} - Balance: ${self.balance}"
            
        
def main():
    account1 = Account('Pedro Romero', Decimal('50.00'))
    print("Initial Account")
    print(account1)
    account1.deposit(Decimal('-500.00'))
    print("Deposit Account")
    print(account1)
    account1.withdrawal(Decimal('200.00'))
    print("Withdrawal Account")
    print(account1)
    

if __name__ == "__main__":
    main()