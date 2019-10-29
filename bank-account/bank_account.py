class BankAccount(object):
    def __init__(self):
        self.accountClosed = True
        self.balance = 0

    def get_balance(self):
        if self.accountClosed:
            raise Exception("Can not get balance on closed account")
        return self.balance

    def open(self):
        self.accountClosed = False
        print("Opening Account")

    def deposit(self, amount):
        if self.accountClosed:
            raise Exception("Can do deposit on closed account")
        print("Account Deposit")
        self.balance = self.balance + amount
        pass

    def withdraw(self, amount):
        if self.accountClosed:
            raise Exception("Can not do withdraw on closed account")
        print("Account Withdraw")
        self.balance = self.balance - amount
        pass

    def close(self):
        self.accountClosed = True
        print("Close Account")
