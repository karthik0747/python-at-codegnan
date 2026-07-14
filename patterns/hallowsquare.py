n=5#i+j=n-1
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
           print( "*",end= "  ") #i+1
        else:
            print(" ",end="  ")
    print()