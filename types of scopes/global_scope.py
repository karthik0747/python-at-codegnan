#global scope
x=10
def outer():
    y=20# enclose 
    def inner():
        z=30 #local scope
        res=z+y+x
        print("this is local scope: {res}")
    res = y+x
    inner()
    print(f" This is enclosing scope: {res}")
outer()