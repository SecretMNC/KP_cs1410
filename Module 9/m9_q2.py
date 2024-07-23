"""Contains logging.
Line #'s for the logging code examples:
9, 10, 185, 188, 192, 195, 207, 210, 214, 217, 229, 232, 236, 239.
"""

import logging
from typing import Protocol

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

class OverdraftError(Exception):
    pass

class MinBalanceError(Exception):
    pass


class BankAccount(Protocol):

    def deposit(self):
        pass

    def withdrawl(self):
        pass

    def calc_interest(self):
        pass
    
class SavingsAccount():
    def __init__(self, balance=0, interest_rate=0.05, remaining_withdrawls=5):
        self.balance = balance
        self.interest_rate = interest_rate
        self.remaining_withdrawls = remaining_withdrawls
        
    def deposit(self, amount: float):
        self.balance += amount
        if self.balance <= 0:
            raise ValueError("Please only enter in a positive number.")
        return f"Deposit of ${amount:.2f} successful. Current balance: {self.balance}."
    
    def withdrawal(self, amount: float):
        if amount <= 0:
            raise ValueError("You many only withdraw a positive amount.")
        check_remainder = self.balance - amount
        if check_remainder < 0:
            raise OverdraftError("The account balance cannot be negative.")
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
    
    def compute_interest(self):
        if self.interest_rate < 0:
            raise ValueError("The interest rate may not be negative.")
        int_amt = self.balance * self.interest_rate
        self.balance += int_amt
        return f"Interest amount of ${int_amt:.2f} has been added to savings. Balance: ${self.balance:.2f}"
    
    def check_withdrawals(self):
        if self.remaining_withdrawls <= 0:
            return False
        else:
            return True
        
    
class MoneyMarketAccount():
    def __init__(self, balance=0, interest_rate=0.03, min_balance=1000):
        self.balance = balance
        self.interest_rate = interest_rate
        self.min_balance = min_balance
    
    def deposit(self, amount: float):
        if self.balance <= 0:
            raise ValueError("Please enter in at least $0.01.")
        self.balance += amount
        return f"Deposit of {amount} successful. Current balance: {self.balance}."
    
    def withdrawal(self, amount: float):
        if amount <= 0:
            raise ValueError("You many only withdraw a positive amount.")
        check_remainder = self.balance - amount
        if check_remainder < 0:
            raise OverdraftError("The account balance cannot be negative.")
        try:
            self.min_balance_check()
        except MinBalanceError as err:
            return err
        else:
            self.balance -= amount
            return f"""Withdrawl of {amount} successful.
Remaining balance: {check_remainder}."""
    
    def compute_interest(self):
        if self.interest_rate < 0:
            raise ValueError("The interest rate may not be negative.")
        int_amt = self.balance * self.interest_rate
        self.balance += int_amt
        return f"Interest amount of ${int_amt:.2f} has been added to Money Market. Balance: ${self.balance:.2f}"
    
    def min_balance_check(self):
        if self.balance < self.min_balance:
            raise MinBalanceError(f"Insufficient funds:\nThe account balance may not be below {self.min_balance}.")
    
class CheckingAccount():
    def __init__(self, balance=0, interest_rate=0.00, min_balance=500):
        self.balance = balance
        self.interest_rate = interest_rate
        self.min_balance = min_balance
    
    def deposit(self, amount: float):
        self.balance += amount
        if self.balance <= 0:
            raise ValueError("Please enter in at least $0.01.")
        return f"Deposit of {amount} successful. Current balance: {self.balance}."
    
    def withdrawal(self, amount: float):
        if amount <= 0:
            raise ValueError("You many only withdraw a positive amount.")
        check_remainder = self.balance - amount
        if check_remainder < 0:
            raise OverdraftError("The account balance cannot be negative.")
        try:
            self.min_balance_check()
        except MinBalanceError as err:
            return err
        else:
            self.balance -= amount
            return f"""Withdrawl of {amount} successful.
Remaining balance: {check_remainder}."""
    
    def calc_interest(self):
        if self.interest_rate < 0:
            raise ValueError("The interest rate may not be negative.")
        self.balance += self.balance * self.interest_rate
    
    def min_balance_check(self):
        if self.balance >= self.min_balance:
            return True
        else:
            raise MinBalanceError(f"The account balance may not be below {self.min_balance}")


my_savings = SavingsAccount(20)
my_mm = MoneyMarketAccount()
my_checking = CheckingAccount()

def compute_interest(acct: BankAccount):
    print(acct.compute_interest())
    
def check_balance(acct: BankAccount):
    print(acct.check_balance())
    
#compute_interest(my_savings)
    
def main():
    my_savings = SavingsAccount()
    my_mm = MoneyMarketAccount()
    my_checking = CheckingAccount()
    
    print("New bank accounts created.")
    
    while True:
        pick_acct = input("""What account would you like to use?
(1): Savings Account
(2): Money Market Account
(3): Checking Account
(4): Quit
""")
        if pick_acct == "1":
            action = input("""What would you like to do in Savings Account?
(1): Deposit
(2): Withdraw
(3): Return to the main menu
""")
            if action == "1":
                try:
                    amount = input("Enter how much money you will be depositing.\n -->")
                    logger.info(f"Passed in deposit amount is {amount}")
                    my_savings.deposit(float(amount))
                except ValueError as err:
                    logger.error(f"ValueError in SavingsAccount obj: {err}")
            elif action == "2":
                try:
                    amount = input("Enter how much money you will be withdrawing.\n -->")
                    logging.info(f"Amount for depositing is {amount}")
                    print(my_savings.withdrawal(float(amount)))
                except ValueError as err:
                    logging.error(f"ValueError in SavingsAccount obj: {err}")           
            else:
                continue
        elif pick_acct == "2":
            action = input("""What would you like to do in Money Market Account?
(1): Deposit
(2): Withdraw
(3): Return to the main menu
""")
            if action == "1":
                try:
                    amount = input("Enter how much money you will be depositing.\n -->")
                    logger.info(f"Passed in deposit amount is {amount}")
                    my_mm.deposit(float(amount))
                except ValueError as err:
                    logger.error(f"ValueError in MoenyMarketAccount obj: {err}")
            elif action == "2":
                try:
                    amount = input("Enter how much money you will be withdrawing.\n -->")
                    logging.info(f"The passed in withdrawl amount is {amount}")
                    print(my_mm.withdrawal(float(amount)))
                except ValueError as err:
                    logging.error(f"ValueError in MoneyMarketAccount obj: {err}")   
            else:
                continue
        elif pick_acct == "3":
            action = input("""What would you like to do in Checking Account?
(1): Deposit
(2): Withdraw
(3): Return to the main menu
""")
            if action == "1":
                try:
                    amount = input("Enter how much money you will be depositing.\n -->")
                    logger.info(f"Passed in deposit amount is {amount}")
                    my_checking.deposit(float(amount))
                except ValueError as err:
                    logging.error(f"ValueError in CheckingAccount obj: {err}")
            elif action == "2":
                try:
                    amount = input("Enter how much money you will be depositing.\n -->")
                    logger.info(f"Passed in withdraw amount is {amount}")
                    print(my_checking.withdrawal(float(amount)))
                except ValueError as err:
                    logging.error(f"ValueError in CheckingAccount obj: {err}")     
            else:
                continue
        elif pick_acct == "4":
            quit()
        else:
            continue

main()
