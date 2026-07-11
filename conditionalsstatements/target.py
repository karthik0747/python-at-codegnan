lst=list(map(int,input().split()))
target=int(input())
if target in lst:
    print("exists")
else:
    print("-1")