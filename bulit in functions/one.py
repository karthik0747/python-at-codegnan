# built in functions: The functions defination is provided by python ,those functions called as built in functions

#abs() : it returns the absolute value
print(abs(20-10))
print(abs(10-20))

#round(val, pos): This function rounds the float value to particular positions
print(round(2.2589,2))
print(round(2.2539,2))
print(round(2.2589))
print(float(2.2589))


#ord(char) : It returns ACSII value of character
#chr(ascii_val): it returns the characters for specified ASCII value
print(ord("A"))
print(chr(65))

#sorted(iterable, reverse = False, Key = None): It returns new sorted iterable
#sort the fruits based on the length of fruit name
fruits = ['apple','banana','kivi','mango','water melon']
res = sorted(fruits)
print(res)
print(sorted(fruits, reverse =True))
print(sorted(fruits, reverse =True,key=len)) # it sorts the list based on length of each items


#map(function, iterable)
#find the square of all list of integers using map function
def square(x):
    return x**2
arr=[1,2,3,4,5]
res= list(map(square,arr))
print(res)
#filter(function, iterable) : it filters the  iterable, if the function returns non -none those values will add to result
#find even numbers from list of numbers 
def check_even(x):
    if x%2==0:
        return 1
lst =[1,2,3,4,5,6]
res = list(filter(check_even,lst))
print(res)

# find the 3's multiples from list of integers
def multiples(x):
    if x%3==0:
        return 1
lst =[1,2,3,4,5,6]
res = list(filter(multiples,lst))
print(res)

#enumerate(iterable) : this function returns the list of tuple of index and item for iterable elements
fruit= ['apple','banana','kivi','mango','water melon']
print(enumerate(fruit))
print(list(enumerate(fruit)))
for ind,val in enumerate(fruit):
    print(f"{ind}-{val} and length is {len(val)}")


#Tuple unpacking
t=(1,2)
a,b=t
print(a,b)

#zip(iterable1, iterable2,..): It returns all itables as single iterable of tuples
roll_no=[101,102,103,104,105]
names= ['ravi','raju','siva','rani','gopi']
percentage =[90,67,96.8,67.65,99.9999]
print(list(zip(roll_no,names,percentage)))


#decimal to binary
num=11
res=""
while num>0:
    bit =num%2
    num =num//2
    res = str(bit)+res
print(res)


#number conversions
print(bin(10))
print(bin(10)[2:])
print(oct(10))
print(hex(11).upper()[2:])

# decimal to hexa
num=12
res=""
while num>0:
    bit =num%16
    num =num//16
    res = str(bit)+res
print(res)


#any (): This function returns true when any one iterable items return true
#all() : This function returns true when all iterable items return true
arr=[1,2,3,4,0]
print(all(arr))
print(any(arr))

'''percentage = [34,35,54,65,67]
for num in percentage:
    if num < 35:
        print("All students not passed")
        break
else:
    print("All students pass")'''

percentage = [34,35,54,65,67]
lst = []
for num in percentage:
    if num < 35:
        lst.append(False)
    else:
        lst.append(True)
print(lst)
if all (lst):
     print("All students not passed")
else:
    print("All students pass")

