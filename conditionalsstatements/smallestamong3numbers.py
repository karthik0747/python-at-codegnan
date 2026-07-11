n0=int(input())
n1=int(input())
n2=int(input())
if n0<n1 and n0<n2:
    print(f"{n0} is the smallest number.")
elif n1<n0 and n1<n2:
    print(f"{n1} is the smallest number.")
else:
    print(f"{n2} is the smallest number.")