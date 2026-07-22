#4 with parameter and with return
#sum of 2 numbers
'''def add(x:int,y:int)->int:
    c=x+y
    return c
res=add(5,6)
print(res)'''


#3 without parameter and with return
#sum of 2 numbers
'''def add()->int:
    x,y=10,20
    c=x+y
    return c
res=add()
print(res)'''

# function not returnsany value  or function doesnt contains return statement
#     in this cose,function by defaulty it returns 'none ' as result to function call block
#2 with parameter and without return
'''def add(x:int,y:int)->int:
    c=x+y
    print(f"this is from function defination block: {c}")
res=add(5,6)
print(f"this is from function defination block: {res}")'''


#1  without parameter and without return
'''def add()->int:
    x,y=10,30
    c=x+y
    print(f"this is from function defination block: {c}")
res=add()
print(f"this is from function defination block: {res}")'''



# number is prime or not
'''def prime(n:int)->bool:
    if n<2:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
num=int(input())
print(prime(num))'''

#print prime numbers from 1 to 100
def prime(n:int)->bool:
    if n<2:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
for j in range(1,100):
    if prime(j):
        print(j,end=" ")
        

        
