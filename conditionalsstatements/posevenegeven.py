n=int(input("Enter a number: "))
if n%2==0:
    if n>0:
        print(f"{n} is a positive even number.")
    else:
        print(f"{n} is a negative even number.")
else:
    if n>0:
        print(f"{n} is a positive odd number.")
    else:
        print(f"{n} is a negative odd number.")
 