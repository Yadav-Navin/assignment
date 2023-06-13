#1. Use iter and next method to access all the elements of a given set using while loop

def f1():
    s=input("Enter the element separeted by comma ")
    i=0
    s=s.split(',')
    it=iter(s)
    while i<len(s):
        print(next(it))
        i+=1

f1()

#2. Create a generator to produce first n odd natural numbers

def f2(n):
    a=1
    while n:
        yield a
        a+=2
        n-=1

s=int(input("Enter the number "))
b=f2(s)
i=0
while i<s:
    print(next(b))
    i+=1


#3. Create a generator to produce first n even natural numbers

def f3(n):
    a=2
    while n:
        yield a
        a+=2
        n-=1

s=int(input("Enter the number "))
b=f3(s)
i=0
while i<s:
    print(next(b))
    i+=1

#4. Create a generator to produce squares of first N natural numbers

def f4(n):
    a=1
    while n:
        yield a**2
        a+=1
        n-=1

s=int(input("Enter the number "))
b=f4(s)
i=0
while i<s:
    print(next(b))
    i+=1


#5. Create a generator to produce first n terms of Fibonacci series

def f5(n):
    a=-1
    b=1
    while n:
        yield a+b
        a,b=b,a+b
        n-=1

s=int(input("Enter the number "))
b=f5(s)
i=0
while i<s:
    print(next(b))
    i+=1


#6. Create a generator to produce first n prime numbers

def f6(n):
    i=2
    while n:
        a=2
        while i>1 and a<i:
            if i%a==0:
                break
            a+=1  
        else:
            yield i
        i+=1
        n-=1

s=int(input("Enter the number "))
# b=f6(s)
for b in f6(s):
    print(b)
# i=0
# while i<s:
#     print(next(b))
#     i+=1

#7. Create an endless iterator using generator method to produce terms of Fibonacci
#series

def f7():
    a=-1
    b=1
    while True:
        yield a+b
        a,b=b,a+b

b=f7()
while True:
    i=input("can you print [y/n] ")
    if i=='n':
        break
    print(next(b))

#8. Create an endless iterator using generator method to produce Prime numbers

def f8():
    i=2
    while True:
        a=2
        while i>1 and a<i:
            if i%a==0:
                break
            a+=1  
        else:
            yield i
        i+=1

b=f8()
while True:
    i=input("can you print [y/n] ")
    if i=='n':
        break
    print(next(b))

'''9. Define a function which takes lengths of three sides of a triangle as arguments and
display the perimeter or triangle. Define and apply a decorator which checks for the
validity of the triangle on the basis of lengths of the side. This makes the perimeter to
be displayed when the triangle can exist with the given lengths of the sides.'''

def valid_trianle(Triangle,a,b,c):
    def check(left_side,base,right_side):
        if a+b>c and b+c>a and c+a>b:
            print("Valid Triagle")
        Triangle(left_side,base,right_side)

@valid_trianle
def Triangle(left_side,base,right_side):
    p=left_side+base+right_side
    print("Perimeter of Triangle is",p)

#10. Define a function which calculates HCF of two numbers. Define and apply a
#decorator to check whether two given numbers are co-prime or not.


def dec_HCF(HCF):
    def co_prime(a,b):
        if a==1 and b==1:
            print('co-prime')
        HCF(a,b)

@dec_HCF
def HCF(a,b):
    i=min(a,b)
    while i:
        if a%i==0 and b%i==0:
            print("HCF is",i)
            break
        i-=1
    
HCF(6,12)