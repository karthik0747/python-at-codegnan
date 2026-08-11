#Linear Search --Time complexity-o(n)
def Lsearch(arr,val):
    for i in range(len(arr)):
        if arr[i]==val:
            return i
    return -1
#driver code
arr=[10,20,3,5,7,8,99]
val=7
result=Lsearch(arr,val)
print(result)