#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
class Account:
    
    def __init__(self):
        self.__balance = 0
        self.accountnumber = "account_" + str(random.randint(1000, 9999))
        
    def __repr__(self):
        return f"{self.accountnumber}|{self.__balance}"
    
    def deposit(self, amount):
        self.__balance += amount
        return(f"${amount} is added to the account, Current: {self.__balance}")
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return(f"You withdrew: ${amount}, Current: {self.__balance}")
        else:
            return("Insufficent founds")
        
    def get_balance(self, accountnumber):
        if self.accountnumber == accountnumber:
            return(f"Accountnumber: {accountnumber} Balance: {self.__balance}")

