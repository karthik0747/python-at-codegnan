users={
        1001:{'name':"dhoni",'gmail':"thala@gmail.com",'balance':5000,'password':'1001'},
        1002:{'name':"msd",'gmail':"msd@gmail.com",'balance':1000,'password':'1002'}
        }


# transfer function
def transfer(sender_account:int,receiver_account:int,transfer_amount:int):
    if receiver_account not in users:
        return "Receiver account does not exist"

    if users[sender_account]['balance'] < transfer_amount:
        return "Insufficient Balance"

    users[sender_account]['balance'] -= transfer_amount
    users[receiver_account]['balance'] += transfer_amount

    return (f"Transfer Successful!\n"
            f"Transferred Amount: {transfer_amount}\n"
            f"Current Balance: {users[sender_account]['balance']}")