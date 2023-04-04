#!/usr/bin/env python
# coding: utf-8

# In[1]:


from MidasBankAccount import Account

class Customer:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.account = []
        self.pw_check = False
        
    def __repr__(self):
        return f"Username: {self.username} \nAccount-list: {self.account}"
    
    def get_customers_to_file(self):
        return f"{self.username}/{self.password}@{self.account}"
    
    def password_check(self, username, password):
        if (self.username == username) and (self.password == password):
            self.pw_check = True
            print(f"Your password is {self.pw_check}")
        
    def make_password_false(self):
        self.pw_check = False
        print(f"You password is now {self.pw_check}")
        
    def add_account(self):
        if self.pw_check == True:
            self.account.append(Account())
            return "Account added"
        
    def get_account(self, accountnumber):
        if self.pw_check == True:
            for account in self.account:
                if account.accountnumber == accountnumber:
                    return account
                else:
                    print(None)
    
    def deposit(self, accountnumber, amount):
        if self.pw_check == True:
            dep = self.get_account(accountnumber)
            if dep:
                return dep.deposit(amount)
                
    def withdraw(self, accountnumber, amount):
        if self.pw_check == True:
            wit = self.get_account(accountnumber)
            if wit:
                return wit.withdraw(amount)

    def get_accounts(self):
        if self.pw_check == True:
            if self.account != 0:
                print(self.account)
            else:
                print(None)
                
    def remove_account(self, accountnumber):
        if self.pw_check == True:
            for account in self.account:
                if account.accountnumber == accountnumber:
                    self.account.remove(account)
                    print(f"{accountnumber} has been safely removed")

