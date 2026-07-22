#types of arguments
#1 . Positional Arguments
'''def sub(x:int,y:int)->int:
    c=x-y
    return c
a,b =map(int,input().split())
res=sub(a,b)
print(res)
print(sub(b,a))'''

#types of arguments
#2 . keyword Arguments : here ARGUMENTS Ppassed along with the parameter
'''def sub(x:int,y:int)->int:
    c=x-y
    return c
a,b =10 , 20
print(sub(x=a, y=b))
print(sub(y=b,x=a))'''


'''def add(a,b):
    s=a+b
    return s
print(add(1,2))


def add(a,b,c):
    s=a+b+c
    return s
print(add(1,2,3))

def add(a,b,c,d):
    s=a+b+c+d
    return s
print(add(1,2,4,5))'''



# 3.default arguments : The parameters defined with some default values and it assigns the argument value f you pass the values for defaults  paraments other wise,I
#       it will assign default values
'''def add(a,b,c=0,d=0):
    res=a+b+c+d
    return res
print(add(10,20))
print(add(10,20,5))
print(add(10,20,2,1))'''


'''def add(a,b,c=1,d=1):
    res=a*b*c*d
    return res
print(add(10,20))
print(add(10,20,5))
print(add(10,20,2,1))'''


#4. variable length of positional arguments
'''def add(a,b=0,*args):
    print(type(args))
    print(args)
    s=0
    for num in args:
        s=s+num
    return s+a+b
print(add(1))
print(add(1,2,3,4,5,6,7,8,9))'''

#5 .variable length of key word arguments
'''def details(name,age,*marks,**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs.keys())
print(details("ravi",20,85,95,75,grnder= "male",location="india"))'''



#pass by value
def fun(x):
    print(x)
    print(f" before address of x :{id(x)}")
    x=x+1
    print(x)
    print(f" after address of x :{id(x)}")
a=5
print(f" before function execution address of a:{id(a)} and value:{a}")
print(fun(a))
print(f" after function execution address of a:{id(a)} and value:{a}")

# pass by refference




'''def fun(x):
    print(x)
    print(f" before address of x :{id(x)}")
    x=x+1
    print(x)
    print(f" after address of x :{id(x)}")
a=5
print(f" before function execution address of a:{id(a)} and value:{a}")
print(fun(a))
print(f" after function execution address of a:{id(a)} and value:{a}")'''
    
