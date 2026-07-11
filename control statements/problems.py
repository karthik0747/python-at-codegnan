#count vowels,consonents,special characters in string
'''k=input().lower()
v=0
c=0
for i in k:
    if i.isalpha():
         if i in 'aeiou':
             v=v+1
         else:
            c=c+1
print(v)
print(c)'''

#count even in lst and odd in list
'''lst=list(map(int,input().split()))
even=[]
odd=[]
for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)

print(odd)'''

#print 1 to n numbers using range function
n=int(input())
for i in range(0,n):
    print(i,end=" ")

