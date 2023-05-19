class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def add_money(self, money):
        self.balance += money
    def get_money(self, money):
        self.balance -= money


account = BankAccount('Ivan Ivanov', 220043046473426, 1302)
account.get_money(200)
print(account.balance)