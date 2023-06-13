'''1. Write a python program to create a user class with 3 properties : name, age, email.'''

class user:
    def __init__(self,name,age,email):
        self._name=name  
        self._age=age
        self._email=email
    def get_user(self):
        return self
    def show_user(self):
        print(self._name,self._age,self._email)
    def youngest_person(self,user2,user3):
        if user2._age>self._age<user3._age:
            return self
        elif self._age>user2._age<user3._age:
            return user2
        else:
            return user3




person1 = user('Navin',21,'navin256@gmail.com')
# person1._age=20
# person1._name='shubham'
# person1._email='shubham34@gmail.com'
a=person1.get_user()
a.show_user()
person2 = user('saurabh',23,'saurabh456@gmail.com')
person3 = user('shivam',20,'shivam23@gmail.com')
c=person1.youngest_person(person2,person3)
c.show_user()
# del person2._age
# person2._age=21
# del person2._age
# person2._name='soni'
# person2._email='soni675@gmail.com'
b=person2.get_user()
b.show_user()
        

'''7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the
values).'''

class Laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd
    
    def config(self):
        print(self.brand,self.ram,self.cpu,self.hdd)
    
    def sorted_by_ram(self,user2,user3):
        print("shorted result")
        if user2.ram>self.ram<user3.ram:
            self.config()
            if user2.ram<user3.ram:
                user2.config()
                user3.config()
            else:
                user3.config()
                user2.config()
        elif self.ram>user2.ram<user3.ram:
            user2.config()
            if self.ram<user3.ram:
                self.config()
                user3.config()
            else:
                user3.config()
                self.config()
        else:
            user3.config()
            if self.ram<user2.ram:
                self.config()
                user2.config()
            else:
                user2.config()
                self.config()

    
lap1 = Laptop('apple',8,'i9','1tb')
lap2 = Laptop('HP',6,'i5','1tb')
lap3 = Laptop('Dell',4,'i7','1tb')
a=lap1.sorted_by_ram(lap2,lap3)


class School:
    name="C.N.Vidhyalay"
    def __init__(self,classroom,teacher):
        self.clssroom=classroom
        self.teacher=teacher
    
    def show(self):
        print(self.clssroom,self.teacher)

a = School(1,'Navin sir')
a.show()

class Employee:
    def __init__(self):
        self.empid=None
        self.name="none"
        self.salary=0.0

    def input(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary
    
    def show(self):
        print(self.empid,self.name,self.salary)

emp = Employee()
emp.input(1,'Navin',2345)
emp.show()
    
