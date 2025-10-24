# Handles a single user account
import datetime
import bcrypt  

class Account:
    def __init__(self, acc_no, name, balance=0, password=""):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.history = []

        # # Only hash if it's not already hashed
        
        
    
    
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"{datetime.datetime.now()}: Deposited {amount}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.history.append(f"{datetime.datetime.now()}: Withdrew {amount}")
            return True
        return False

    def get_details(self):
        return {
            "acc_no": self.acc_no,
            "name": self.name,
            "password": self.password,
            "balance": self.balance,
            "history": self.history
        }

    @staticmethod
    def from_dict(data):
        acc = Account(data["acc_no"], data["name"], data["balance"], data.get("password", ""))
        acc.history = data.get("history", [])
        return acc
