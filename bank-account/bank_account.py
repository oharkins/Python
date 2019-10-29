class BankAccount(object):
    def __init__(self):
        self.accountClosed = True
        self.balance = 0

    def get_balance(self):
        if self.accountClosed:
            raise Exception("Can not get balance on closed account")
        return self.balance

    def open(self):
        if not self.accountClosed:
            raise Exception("Can not open a opened account")
        self.accountClosed = False

    def deposit(self, amount):
        if self.accountClosed:
            raise Exception("Can not do deposit on closed account")
        if amount < 0:
            raise Exception("Can not deposit negative amount")

        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.accountClosed:
            raise Exception("Can not do withdraw on closed account")

        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            raise Exception("Can not withdraw more than balance")

    def close(self):
        if self.accountClosed:
            raise Exception("Can not close a closed account")
        self.accountClosed = True
        self.balance = 0
