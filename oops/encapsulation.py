#create mobile class
'''class Mobile:
    company="Iphone"
    def __init__(self,model,ram,rom,price):
        self.model=model
        self.ram=ram
        self.rom=rom
        self.price=price
#object creation
iphone16=Mobile("iphone 16",16,256,125000)
iphone17=Mobile("iphone 17",8,256,120000)-
print(iphone16.price)
print(iphone17.price)
print(iphone16.company)
print(iphone17.company)
print(Mobile.company)'''

#updating instance attribute data from outside class
'''class Mobile:
    company="Iphone"
    def __init__(self,model,price,ram=8,rom=256):
        self.model=model
        self.ram=ram
        self.rom=rom
        self.price=price

#object creation
iphone16=Mobile("iphone 16",80000)
iphone17=Mobile("iphone 17",120000,16)
print(iphone16.ram)
iphone16.ram=16
print(iphone16.ram)
iphone16.company="New Iphone"
print(iphone16.company,iphone17.company)'''



'''class Mobile:
    company="Iphone"
    def __init__(self,model,ram,rom,price):
        self.model=model
        self.ram=ram
        self.rom=rom
        self.price=price
    def about_phone(self):
        return f"The {self.model} have {self.ram} GB RAM and {self.rom} GB ROM" 
    def display():
        return "This is samsung display"
#object creation
iphone16=Mobile("iphone 16",16,256,125000)
iphone17=Mobile("iphone 17",8,256,120000)
print(iphone16.about_phone())'''



'''class Mobile:
    company="Iphone"
    def __init__(self,model,ram,rom,price):
        self.model=model
        self.ram=ram
        self.rom=rom
        self.price=price
    def about_phone(self):
        return f"The {self.model} have {self.ram} GB RAM and {self.rom} GB ROM" 
    def display():
        return "This is samsung display"
    #class method
    @classmethod
    def update_company(cls,new_name):
        cls.company=new_name
        return "Company name updated"
    #static method
    @staticmethod
    def charger_provide(cable=True):
        return "adpter + cable" if cable else "adpter"
#object creation
iphone16=Mobile("iphone 16",16,256,125000)
iphone17=Mobile("iphone 17",8,256,120000)
print(iphone16.about_phone())
print(iphone16.update_company("Iphone pro"))
print(iphone16.charger_provide())'''


'''class Mobile:
    company="Iphone"
    def __init__(self,model,ram,rom,price):
        self.model=model
        self.ram=ram
        self.rom=rom
        self.price=price
    def about_phone(self):
        return f"The {self.model} have {self.ram} GB RAM and {self.rom} GB ROM" 
    def display():
        return "This is samsung display"
    #class method
    @classmethod
    def update_company(cls,new_name):
        cls.company=new_name
        return "Company name updated"
    #static method
    @staticmethod
    def charger_provide(cable=True):
        return "adpter + cable" if cable else "adpter"
#object creation
iphone16=Mobile("iphone 16",16,256,125000)
iphone17=Mobile("iphone 17",8,256,120000)
#print(Mobile.about_phone())
print(Mobile.update_company("Iphone pro"))
print(Mobile.charger_provide())
print(Mobile.company)'''


'''class Account:
    bank_name="Karthik"
    def __init__(self,username,balance,password):

        self.username=username
        self.balance=balance
        self.password=password
    def withdraw(self,amount):
        if self.balance >= amount:
             self.balance -=amount
             return f"{amount} withdrawal successfully"
        return "Insufficient Balance"
    def deposit(self,amount):
            self.balance+=amount
            return f"{amount} deposite successfully and curr balance is {self.balance}"
    def total_users(self):
         return "Total users:100"
user=Account("karthik",5000,"kar@123")
print(user.deposit(1000))
user.balance=100000
print(user.withdraw(50000))'''

# Access Modifier Example

class Account:
    bank_name = "Karthik"

    def __init__(self, username, balance, password):
        self.username = username        # Public
        self._balance = balance         # Protected
        self.__password = password      # Private

    def update_password(self, new_password):   # Setter method
        self.__password = new_password
        return "Password updated"

    def get_password(self):             # Getter method
        return self.__password

    def get_balance(self):              # Getter method
        return self._balance

    def withdraw(self, amount):         # Setter method
        if self._balance >= amount:
            self._balance -= amount
            return f"{amount} withdrawn successfully"
        return "Insufficient Balance"

    def deposit(self, amount):          # Setter method
        self._balance += amount
        return f"{amount} deposited successfully and current balance is {self._balance}"

    def __total_users(self):            # Private method
        return "Total users: 100"


user = Account("karthik", 5000, "kar@123")

print(user.username)
print(user.get_balance())
print(user.deposit(5000))
print(user.update_password("kkk@123"))
print(user.get_password())

# Access the protected member
print(user._balance)

# Access the private method using name mangling
print(user._Account__total_users())


    







