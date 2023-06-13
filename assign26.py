from time import *
import time
import random

'''
1. Write a python script to multiple 2 or 3 or 4 numbers with a single multiply method in
a class using method overloading.'''


class overloading:
    def __multipie__(self,a,b,c=1,d=1):
        return a*b*c*d

over = overloading()
a=over.__multipie__(4,5)
print(a)

'''
2. Write a python script to create a user account class with 2 instance variables (userid
and balance). Create 3 user objects and add all the users using operator
overloading.'''

class user_account:

    def __init__(self,userid,balance):
        self.user_id=userid
        self.balance=balance
    
    def add(self,obj1,obj2):
        return self.balance+obj1.balance+obj2.balance

    def hint__str__method(self,obj1,obj2):
        print("first user",self.user_id,self.balance)
        print("second user",obj1.user_id,obj1.balance)
        print("third user",obj2.user_id,obj2.balance)


p = user_account(204848,5467.90)
p1 = user_account(436576,123406.45)
p2 = user_account(56784,67849.10)
bal = p.add(p1,p2)
print(bal)
       

'''
4. Write a python script to create two Threads. First thread will print all Even numbers
and Second thread will print all Odd numbers till 100.'''

class threads:

    def Even(self):
        for e in range(1,100):
            if e%2==0:
                print(e,end=' ')
        sleep(1)
        print("-----------------------------")

class threads1:
    def odd(self):
        for i in range(1,100):
            if i%2!=0:
                print(i,end=' ')
        sleep(1)
        print("*********************************")

th = threads()
th.Even()
sleep(2)
print("Thanks")
th1 = threads1()
th1.odd()


'''
5. Write a python script to create 2 threads to add all the values from 1 to 100.'''

class add:
     
    def add(self):
        s=0
        for i in range(1,101):
            s = s + i
            print(s,end=' ')
            sleep(1)

a = add()

a.add()
sleep(5)
print("hello")


'''6. Write a python script to create 5 threads to fill a list with random numbers till 100.
'''

class randthread:
    def rand(self):
        sleep(3)
        for i in random.randrange(1,100):
            print(i)
ra = randthread()
ra.rand()

'''7. Write a python script to create a clock where 1st thread will print the current time
every second and 2nd will print “1 Minute Completed” after every 1 minute.
'''

'''8. Write a python script to change the name of the Thread.
9. Write a python script to join 2 threads after printing completing the first Question.
10. Write a python script to check whether a given number is prime or armstrong number
using 2 different threads.
'''