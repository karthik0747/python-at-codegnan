#1.Single Inheritance
#when child class dont have constructor, In this case parent class constructor behaves like child class constructor
#with implementation in child class
#parent class
'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        return f"My name is {self.name} and I am a {self.age} years old"
#child class
class Student(Person):
    pass

s=Student("ravi",20)
print(s.name)
print(s.details())'''



# parent class
'''class person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def details(self):
        return f"My name is {self.name} and I am a {self.age} years old and {self.gender}"
#child class
class student(person):
    def __init__(self,stdid,name,age):
        self.stdid = stdid
        self.name = name
        self.age = age
p = person("kishore",21,"Male")  
s = student(101,"ravi",20)
print(s.name)
print(p.details())
s.gender = "male" # Adding new instancs attribute
print(s.details())'''



# Inherete the parent class constructor in child class by using super()
# parent class
'''class person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def details(self):
        return f"My name is {self.name} and I am a {self.age} years old and {self.gender}"
#child class
class student(person):
    def __init__(self,stdid,name,age,gender):
        self.stdid = stdid
        super().__init__(name,age,gender)
    def percentage(self,marks:list):
        return sum(marks)/len(marks)
s = student(101,"ravi",20,"male")
print(s.name)
print(s.details())
print(s.percentage([90,89,88]))'''

# Multilevel Inheritance

'''class Employee:
    company = "Blitzz"

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def calculate_salary(self, bonus=0):
        return self.salary + bonus


class TeamLead(Employee):
    def __init__(self, id, name, salary, project_name):
        super().__init__(id, name, salary)
        self.project_name = project_name

    def project_status(self, status):
        return f"{self.project_name} project status: {status}% completed"


class Manager(TeamLead):
    def __init__(self, id, name, salary, project_name, no_projects):
        super().__init__(id, name, salary, project_name)
        self.no_projects = no_projects

    def manager_details(self):
        return f"Managing {self.no_projects} projects"


e = Employee(7, "Thala", 35000)
t = TeamLead(9, "Jaddu", 45000, "Practice Tracking Project")
m = Manager(47, "Karthik", 55000, "Exam Portal Project", 5)

print(e.name, t.name, m.name)
print(e.calculate_salary())
print(t.calculate_salary(5000))
print(t.project_status(90))
print(m.calculate_salary(10000))
print(m.project_status(80))'''

#multiple inheritance
'''class Father:
    def __init__(self,father_name):
        self.father_name=father_name
    def working1(self):
        return f" Father working as engineer"
class Mother:
    def __init__(self,mother_name):
        self.mother_name=mother_name
    def working2(self):
            return f" mother working as engineer"
class child(Father,Mother):
    def __init__(self, name,father_name,mother_name):
        self.name=name
        Mother.__init__(self,mother_name)
        Father.__init__(self,father_name)
    def working(self):
         print(super().working1())
         print(super().working2())
c=child("srinu","satya","mahi")
print(c.father_name)
print(c.mother_name)
print(child.__mro__)#Method resolution order
print(c.working())'''


#Hybrid Inheritance
'''class person:
    def __init__(self, name):
        self.name = name

    def details(self):
        return f"Name: {self.name}"


class student(person):
    def __init__(self, name, stdid):
        person.__init__(self, name)
        self.stdid = stdid

    def study(self):
        return "Studying"


class employee(person):
    def __init__(self, name, empid):
        person.__init__(self, name)
        self.empid = empid

    def work(self):
        return "Working"


class intern(student, employee):
    def __init__(self, name, stdid, empid):
        student.__init__(self, name, stdid)
        employee.__init__(self, name, empid)

    def info(self):
        print(self.details())
        print(self.study())
        print(self.work())


i = intern("UK", 102, 202)

print(i.stdid)
print(i.empid)
i.info()'''


#hierarchical inheritance
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        return f"Name: {self.name}, Age: {self.age}"


class student(person):
    def __init__(self, name, age, stdid):
        self.stdid = stdid
        super().__init__(name, age)

    def study(self):
        return "Studying Python"


class employee(person):
    def __init__(self, name, age, empid):
        self.empid = empid
        super().__init__(name, age)

    def work(self):
        return "Working in Google"


s = student("MSD", 21, 101)
e = employee("THALA", 25, 201)

print(s.details())
print(s.study())

print(e.details())
print(e.work())

            