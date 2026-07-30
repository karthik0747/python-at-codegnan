
users={
        1001:{'name':"dhoni",'gmail':"thala@gmail.com",'balance':5000,'password':'1001'},
        1002:{'name':"msd",'gmail':"msd@gmail.com",'balance':1000,'password':'1002'}
        }

# get balance
def get_balance(account:int)-> str:
    curr_balance = users[account]['balance']
    return f"Current Balance is:{curr_balance}"