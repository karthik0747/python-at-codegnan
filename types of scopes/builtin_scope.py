'''x=10   #global scope
def outer():
    x=20
    x=x+1
    print("this is local scope val:",x)
outer()
print("this is global scope:",x)'''


x=10   #global scope
def outer():
    global x
    x=x+1
    print("this is local scope val:",x)
outer()
print("this is global scope:",x)