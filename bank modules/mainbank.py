import register
import login
import getbalance
import deposit
import transfer
import ministatement
import logout
import withdraw


# main
if __name__=="__main__":
    print("welcome to the Mini Bank")
    print("1.login \n 2. Register")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        # call login function
        account = int(input("Enter your account number: "))
        password = input("Enter your password: ")
        login_val = login.login(account = account,password = password)
        while login_val:

            print("1. Get Balance \n 2. Withdraw \n 3. Deposit \n 4. Transfer \n 5. Mini Statement \n 6. Logout")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                # call balance function
                print(getbalance.get_balance(account = account))
            elif choice == 2:
                amount = int(input("Enter withdraw amount:"))
                print(withdraw.withdraw(account = account,withdraw_amount = amount))
            elif choice == 3:
                amount = int(input("Enter deposit amount:"))
                print(deposit.deposit(account = account,deposit_amount = amount))
            elif choice == 4:
                receiver_account = int(input("Enter receiver account number:"))
                amount = int(input("Enter transfer amount:"))
                print(transfer.transfer(sender_account = account,receiver_account = receiver_account,transfer_amount = amount))
            elif choice == 5:
                print(ministatement.mini_statement(account = account))
            elif choice == 6:
                print(logout.logout())
            else:
                print("Select your choice in between 1 to 6")

        else:
            print("Invalid login credevtials")
    elif choice == 2:
        username = input("Enter user name:")
        email = input("Enter user mail id")
        initial_deposite = int(input("Enter the initial deposite amount:"))
        password = input("Enter your new password:")
        print(register.register(username=username,
                       email=email,
                       balance=initial_deposite,
                       password=password))
    else:
        print("Invalid choice,please select 1 or 2")