n=5
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
           print( "*",end= "  ") #i+1
        else:
            print(" ",end="  ")
    print()