#importing requried modules 
#import port module
import addition
#importing function
from subtraction import sub
#importing module with alias name
import multiplication as mul
#importing function with alias name
from division import div as DIV
if __name__=="__main__":
    print("Welcome to small calculator")
    while True:
        print("1.addition \n 2.subtraction \n 3.multiplication \n 4.division \n 5.exit")
        choice=int(input())
        if choice ==1:
            a,b=map(int,input("enter two number with seperated by space:").split())
            res=addition.add(x=a,y=b)
            print(f"Addition of {a} and {b} is : {res}")
        elif choice==2:
            a,b=map(int,input("enter two number with seperated by space:").split())
            res=sub(x=a,y=b)
            print(f"subtraction of {a} and {b} is : {res}")
        elif choice==3:
            a,b=map(int,input("enter two number with seperated by space:").split())
            res=mul.mult(x=a,y=b)
            print(f"multiplication of {a} and {b} is : {res}")
        elif choice==4:
            a,b=map(int,input("enter two number with seperated by space:").split())
            res=DIV(x=a,y=b)
            print(f"Division of {a} and {b} is : {res}")
        elif choice==5:
            print("Thanks for using small calci")
        else:
            print("invalid")