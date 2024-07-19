# This is skeleton code!
from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdrawl(self):
        pass

    @abstractmethod
    def calc_interest(self):
        pass
    
class SavingsAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0.05, remaining_withdrawls=5):
        self.balance = balance
        self.interest_rate = interest_rate
        self.remaining_withdrawls = remaining_withdrawls
        
    def deposit(self, amount: float):
        self.balance += amount
        return f"Deposit of {amount} successful. Current balance: {self.balance}."
    
    def withdrawl(self, amount: float):
        check_remainder = self.balance - amount
        if self.check_withdrawls() and check_remainder >= 0:
            self.balance -= amount
            self.remaining_withdrawls -= 1
            return f"""Withdrawl of {amount} successful.
Remaining balance: {check_remainder}.
Remaining withdrawls: {self.remaining_withdrawls}."""
        elif self.check_withdrawls() and check_remainder < 0:
            return "Insufficient funds."
        elif self.remaining_withdrawls <= 0:
            return "You are out of withdrawls for the month."
    
    def calc_interest(self):
        self.balance += self.balance * self.interest_rate
    
    def check_withdrawls(self):
        if self.remaining_withdrawls <= 0:
            return False
        else:
            return True
    
class MoneyMarketAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0.03, min_balance=1000):
        self.balance = balance
        self.interest_rate = interest_rate
        self.min_balance = min_balance
    
    def deposit(self):
        self.balance += amount
        return f"Deposit of {amount} successful. Current balance: {self.balance}."
    
    def withdrawl(self):
        check_remainder = self.balance - amount
        if self.min_balance_check():
            self.balance -= amount
            return f"""Withdrawl of {amount} successful.
Remaining balance: {check_remainder}."""
        else:
            return "Insufficient funds."
    
    def calc_interest(self):
        self.balance += self.balance * self.interest_rate
    
    def min_balance_check(self):
        if self.balance >= self.min_balance:
            return True
        else:
            return False
    
class CheckingAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0.00, min_balance=500):
        self.balance = balance
        self.interest_rate = interest_rate
        self.min_balance = min_balance
    
    def deposit(self):
        self.balance += amount
        return f"Deposit of {amount} successful. Current balance: {self.balance}."
    
    def withdrawl(self):
        check_remainder = self.balance - amount
        if self.min_balance_check():
            self.balance -= amount
            return f"""Withdrawl of {amount} successful.
Remaining balance: {check_remainder}."""
        else:
            return "Insufficient funds."
    
    def calc_interest(self):
        self.balance += self.balance * self.interest_rate
    
    def min_balance_check(self):
        if self.balance >= self.min_balance:
            return True
        else:
            return False

def main():
    my_savings = SavingsAccount()
    my_mm = MoneyMarketAccount()
    my_checking = CheckingAccount()
    
    print("New bank accounts created.")
    
    while True:
        pick_acct = input(
"""What account would you like to use?
(1): Savings Account
(2): Money Market Account
(3): Checking Account
(4): Quit
""")
        if pick_acct == "1":
            action = input(
"""What would you like to do in Savings Account?
(1): Deposit
(2): Withdraw
(3): Return to the main menu
""")
            if action == "1":
                amount = input("Enter how much money you will be depositing.\n -->")
                my_savings.deposit(float(amount))
            elif action == "2":
                amount = input("Enter how much money you will be withdrawing.\n -->")
                print(my_savings.withdrawl(float(amount)))
            else:
                continue
        elif pick_acct == "2":
            action = input(
"""What would you like to do in Money Market Account?
(1): Deposit
(2): Withdraw
(3): Return to the main menu
""")
        elif pick_acct == "3":
            action = input(
"""What would you like to do in Money Market Account?
(1): Deposit
(2): Withdraw
(3): Return to the main menu
""")
        elif pick_acct == "4":
            quit()
        else:
            continue

main()
