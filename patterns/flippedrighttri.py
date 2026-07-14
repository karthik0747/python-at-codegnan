n=5#i+j=n-1
for i in range(n):
    for j in range(n):
        if j>=n-1-i:
           print( "*",end= "  ") #i+1
        else:
            print(" ",end="  ")
    print()