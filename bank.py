#Manages all accounts and handles saving/loading data from disk.
import json
import os
from account import Account

DATA_FILE = "data.json"

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_data()

    def generate_acc_no(self):
        if self.accounts:
            return max(self.accounts.keys()) + 1
        return 1001  # Starting account number

    def add_user(self, name, balance=0, password=""):
        acc_no = self.generate_acc_no()
        acc = Account(acc_no, name, balance, password)
        self.accounts[acc_no] = acc
        self.save_data()
        return acc_no

    def delete_user(self, acc_no):
        if acc_no in self.accounts:
            del self.accounts[acc_no]
            self.save_data()
            return True
        return False

    def deposit(self, acc_no, amount):
        acc = self.accounts.get(acc_no)
        if acc and acc.deposit(amount):
            self.save_data()
            return True
        return False

    def withdraw(self, acc_no, amount):
        acc = self.accounts.get(acc_no)
        if acc and acc.withdraw(amount):
            self.save_data()
            return True
        return False

    def get_balance(self, acc_no):
        acc = self.accounts.get(acc_no)
        return acc.balance if acc else None

    def get_history(self, acc_no,):
        acc = self.accounts.get(acc_no)
        name = self.accounts[acc_no].name
        return acc.history, name if acc else None
        

    def save_data(self):
        data = {acc_no: acc.get_details() for acc_no, acc in self.accounts.items()}
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                for acc_no, acc_data in data.items():
                    self.accounts[int(acc_no)] = Account.from_dict(acc_data)
