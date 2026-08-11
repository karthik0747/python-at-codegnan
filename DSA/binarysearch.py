# def bsearch(arr,i,j,val):
#     mid=(i+j)//2
#     while i<=j:
#         if arr[mid]==val:
#             return mid
#         elif arr[mid]>val:
#           #recursion
#           return bsearch(arr,i,mid-1,val)#j=mid-1
#         else:
#           #recursion 
#           return bsearch(arr,mid+1,j,val)#i=mid+1
#     return -1
# #driver code 
# arr=[1,2,3,4,5,6,7,8,9]
# val=5
# i=0
# j=len(arr)-1
# res=bsearch(arr,i,j,val)
# print(res)


#rotate an array
arr=[1,2,3,4,5]
k=2
n=len(arr)
for rotate in range(k):
    last=arr[-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=last
print(arr)