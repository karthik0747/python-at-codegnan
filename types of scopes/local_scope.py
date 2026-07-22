#local scope
#we can access the local scope variable within the scope variable within the scope, we cant access in global scope
def fun(x):
    x=x+1
    return x
a=10
res=fun(a)
print(res)