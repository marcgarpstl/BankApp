#!/usr/bin/env python
# coding: utf-8

# In[2]:


from MidasBankAccount import Account
from MidasBankCostumer import Customer

class Bank:
    
    def __init__(self):
        self.customers = []
        self.access = None
        
        
    def __repr__(self):
        return f"I am GOD"
    
    def get_customers(self):
        if len(self.customers) != 0:
            print("All costumers")
            print(self.customers)
        else:
            print(None)
            
    def add_customers_from_file(self):
        a = open("CustomersBank.txt", "r")
        add = a.readlines()
        for customer in add:
            print(customer)
            print("\n")
            userAndPass = customer.split("@")[0].split("/")
            self.add_customer(userAndPass[0], userAndPass[1])
        

    def add_customer(self, username, password):
        self.customers.append(Customer(username, password))
        print(f"Welcome to MidasBank {username}")
    
    def get_customer(self, username):
        for customer in self.customers:
            if customer.username == username:
                return customer
            else:
                print(None)
    
    def change_customer_password(self, username, new_password):
        for customer in self.customers:
            if customer.username == username:
                customer.password = new_password
                return True
            return False
    
    def remove_customer(self, username):
        for customer in self.customers:
            if customer.username == username:
                self.customers.remove(customer)
                print(f"{username} has been safely removed")
    
    def login(self, username, password):
        for customer in self.customers:
            if (customer.username == username) and (customer.password == password):
                self.access = customer
                print("Success")
            
    def logout(self):
        self.rewrite_txt_file()
        print(f"Logging out")
        
        self.access = None
        
    def pw_check(self, username, password):
        if self.access:
            return self.access.password_check(username, password)
        
    def make_false(self):
        if self.access:
            return self.access.make_password_false()
    
    def get_accounts(self):
        if self.access:
            return self.access.get_accounts()
                
    def add_account(self):
        if self.access:
            return self.access.add_account()
    
    def remove_account(self, accountnumber):
        if self.access:
            return self.access.remove_account(accountnumber)
    
    def get_account(self, accountnumber):
        if self.access:
            return self.access.get_account(accountnumber)
    
    def deposit(self, accountnumber, amount):
        dep = self.get_account(accountnumber)
        if dep:
            return dep.deposit(amount)
    
    def withdraw(self, accountnumber, amount):
        wit = self.get_account(accountnumber)
        if wit:
            return wit.withdraw(amount)
        
    def rewrite_txt_file(self):
        rewrite = open("CustomersBank.txt", "r")
        for customer in rewrite.readlines():
            with open ("CustomersBank.txt", "w") as file:
                for customer in god.customers:
                    file.write(customer.get_customers_to_file())
                    file.write("\n")
                    file.flush()


# In[3]:


god = Bank()


# In[4]:


god.add_customers_from_file()


# In[5]:


god.get_customers()


# In[6]:


god.add_customer("Alex", "Great")


# In[7]:


god.get_customer("King")


# In[8]:


god.change_customer_password("King", "Silver")


# In[9]:


god.remove_customer("Alex")


# In[10]:


god.login("King", "Silver")


# In[11]:


god.pw_check("King", "Silver")


# In[12]:


god.add_account()
god.add_account()


# In[15]:


god.get_accounts()


# In[16]:


god.remove_account("account_5363")


# In[17]:


god.deposit("account_9200", 400)


# In[18]:


god.withdraw("account_9200", 350)


# In[19]:


god.withdraw("account_9200", 350)


# In[20]:


god.get_account("account_9200")


# In[21]:


god.logout()


# In[ ]:




