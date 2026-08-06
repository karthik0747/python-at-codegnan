#method overriding
'''class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        return f"person name is {self.name} and his age is {self.age}"
class student(person):
    def __init__(self, name, age,rollno):
        self.rollno=rollno
        super().__init__(name, age)
    def details(self):
        return f"i am a student"
s=student("karthik",21,235)
p=person("ramesh",70)
print(p.details())
print(s.details())'''


'''class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        return f"person name is {self.name} and his age is {self.age}"
class student(person):
    def __init__(self, name, age,rollno):
        self.rollno=rollno
        super().__init__(name, age)
    def details(self):
        #print(super().details())
        return super().details() + f" i am a student"
s=student("karthik",21,235)
p=person("ramesh",70)
#print(p.details())
print(s.details())'''


#method overloading
'''class math:
    def add(x,y):
        return x+y
    def add(x,y,z):
        return x+y+z
    def add(a,b,c,d):
        return a+b+c+d
print(math.add(1,2,3,4))
#print(math.add(1,2,3))
#print(math.add(1,2))'''




#python directing doesnot support method overloading,but we can achive through the default arguments or arbitary arguments
'''class math:

    def add(a,b,c=0,d=0):
        return a+b+c+d
print(math.add(1,2,3,4))
print(math.add(1,2,3))
print(math.add(1,2))'''


#operator overloading
'''class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
p1=point(5,3)
print(p1)


#operator overloading
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):#string magic method
        return f"This point class and value is:({self.x},{self.y})"
p1=point(5,3)
print(p1)'''


'''class point:
    def __init__(self,x):
        self.x=x
        
    def __str__(self):#string magic method
        return f"This point class and value is:({self.x})"
p1=point(5)
p2=point(3)
print(p1.x+p2.x)'''


'''class point:
    def __init__(self,x):
        self.x=x
        
    def __str__(self):#string magic method
        return f"This point class and value is:({self.x})"
    def __add__(self, other):
        return self.x+other.x
p1=point(5)
p2=point(3)
print(p1.x+p2.x)
print(p1+p2)'''


class point:
    def __init__(self,x):
        self.x=x
        
    def __str__(self):#string magic method
        return f"This point class and value is:({self.x})"
    def __add__(self, other):
        return str(self.x)+str(other.x)
    def __sub__(self, other):
            return self.x-other.x

p1=point(5)
p2=point(3)
print(p1.x+p2.x)
print(p1+p2)
print(p1-p2)



