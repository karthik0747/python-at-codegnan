#enclosing scope
def outer(x):
    y=10 #Enclose scope
    def inner():
        a=10 # local scope
        z=y+a
        print(f" This is local scope:{z}")
    inner()
    y=y+x
    print(f"This is enclosing scope:{y}")
n=5
outer(n)