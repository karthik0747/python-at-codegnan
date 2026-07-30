users={
        1001:{'name':"dhoni",'gmail':"thala@gmail.com",'balance':5000,'password':'1001'},
        1002:{'name':"msd",'gmail':"msd@gmail.com",'balance':1000,'password':'1002'}
        }

# login function
def login(account:int,password:str)-> bool:
    if account in users:
        if users [account]['password'] == password:
            return True
        return False
    return False