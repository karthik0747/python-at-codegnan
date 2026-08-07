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
print(p.details())
print(s.details())'''


#method overloading
'''class math:
    def add(x,y):
        return x+y
    def add(x,y,z):
        return x+y+z
    def add(a,b,c,d):
        return a+b+c+d
print(math.add(1,2,3,4))'''





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


'''class point:
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
print(p1-p2)'''


class point:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return str(self.x)

    # Arithmetic Operators
    def __add__(self, other):
        return point(self.x + other.x)

    def __sub__(self, other):
        return point(self.x - other.x)

    def __mul__(self, other):
        return point(self.x * other.x)

    def __truediv__(self, other):
        return point(self.x / other.x)

    def __floordiv__(self, other):
        return point(self.x // other.x)

    def __mod__(self, other):
        return point(self.x % other.x)

    def __pow__(self, other):
        return point(self.x ** other.x)

    # Unary Operators
    def __neg__(self):
        return point(-self.x)

    def __pos__(self):
        return point(+self.x)

    def __abs__(self):
        return abs(self.x)

    # Relational Operators
    def __eq__(self, other):
        return self.x == other.x

    def __ne__(self, other):
        return self.x != other.x

    def __lt__(self, other):
        return self.x < other.x

    def __le__(self, other):
        return self.x <= other.x

    def __gt__(self, other):
        return self.x > other.x

    def __ge__(self, other):
        return self.x >= other.x


p1 = point(10)
p2 = point(3)

print("Addition:", p1 + p2)
print("Subtraction:", p1 - p2)
print("Multiplication:", p1 * p2)
print("Division:", p1 / p2)
print("Floor Division:", p1 // p2)
print("Modulus:", p1 % p2)
print("Power:", p1 ** p2)

print("Negative:", -p1)
print("Positive:", +p1)
print("Absolute:", abs(point(-10)))

print("Equal:", p1 == p2)
print("Not Equal:", p1 != p2)
print("Less Than:", p1 < p2)
print("Less Than or Equal:", p1 <= p2)
print("Greater Than:", p1 > p2)
print("Greater Than or Equal:", p1 >= p2)
