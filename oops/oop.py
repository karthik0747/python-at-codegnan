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
iphone17=Mobile("iphone 17",8,256,120000)
print(iphone16.price)
print(iphone17.price)
print(iphone16.company)
print(iphone17.company)
print(Mobile.company)'''

#updating instance attribute data from outside class
class Mobile:
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
print(iphone16.company,iphone17.company)