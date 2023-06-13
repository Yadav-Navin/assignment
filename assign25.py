'''1. Write a python script to create a Profile class with 3 attributes (name, email, age).'''

class profile:
    platform = 'Unknown'

    def __init__(self):
        self.name = "None"
        self.__email = "None"
        self.__age = 0
    
    def update_profile(self,name,email,age):
        self.name = name
        self.age = age
        self.email = email

    @classmethod
    def access_classmethod(cls,platform):
        cls.platform = platform

p = profile()
p.access_classmethod('Navin')


'''5. Write a python script to create a Calculator class with 2 methods for adding and
subtracting 2 values.'''

class Calculator:

    def __add__(self,a,b):
        return a+b

    def __sub__(self,a,b):
        return a-b
    

class Calculator2(Calculator):

    def __mul__(self,a,b):
        return a*b
    
    def __div__(self,a,b):
        return a/b


add = Calculator()
mul = Calculator2()

a = mul.__mul__(5,4)
print(a)


'''7. Write a python script to create a Phone class with 2 methods to print the features
(calling and sms).'''

class Phone:

    def calling(self):
        print("calling...")
    
    def sms(self):
        print("sms sending...")

cal = Phone()
cal.calling()
cal.sms()




'''
9. Write a python script to create an application like Truecaller where names and
numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a
number and 2nd to add a new entry).'''

class Truecaller:
    def __init__(self):
        self.name = "none"
        self.number = 0000000

    def featch_nameof_number(self):
        print("featching name and number")
    def add(self):
        print("adding new entry")
    
t = Truecaller()
t.featch_nameof_number()
t.add()

'''
10. Write a python script to add the new method in SmartPhone class which accepts
Truecaller object as a parameter and call the fetch method of Truecaller.'''


class SmartPhone(Calculator2,Phone):
    def smart(self):
        print("smart class")
    
    def feature(self,obj):
        obj.featch_nameof_number()

s = SmartPhone()
s.feature(t)
s.smart()
s.calling()
s.sms()