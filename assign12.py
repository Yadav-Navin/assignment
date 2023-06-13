#1.write a python script to reverse a number.

a=int(input("Enter the three digit number "))
while a>0:
    re=a%10
    print(re,end='')
    a=int(a/10)

#2.write a python script to check whether a given
#number is prime or not.

a=int(input("Enter the number "))
i=2
while i>1 and i<a:
    if a%i==0:
        print("Not Prime")
        break
    i+=1
else:
    print("prime")

#3.write a python script to print all prime number under 100.

print("All prime number under 100")
k=2
while k<100:
    count=0
    i=2
    while i<k:
        if k%i==0:
            count=1
        i+=1
    if count==0:
        print("%d"%k)
    k+=1

#4.write a python script to print all prime number between two given numbers(both value inclusive).

a=int(input("Enter first number "))
b=int(input("Enter the second number "))

k=a
while k<=b:
    count=0
    i=2
    while i<k:
        if k%i==0:
            count=1
        i+=1
    if count==0:
        print("%d"%k)
    k+=1

#5.write a python script to find next prime number of a given number.

a=int(input("Enter prime number "))
print("Next prime number")
a+=1
while a:
    count=0
    i=2

    while i<a and count==0:
        if a%i==0:
            count=1
        i+=1
    if count==0:
        print("%d"%a)
        break
    a+=1

#6.write a python script to print first N prime numbers.

a=int(input("Enter number of prime "))
l=1
k=2
while l<=a:
    count=0
    i=2
    while i<k:
        if k%i==0:
            count=1
        i+=1
    if count==0:
        print("%d"%k)
        l+=1
    k+=1

#7.write a python script to check whether a given pair of numbers are co-prime
#numbers or not.

a=int(input("Enter the number "))
b=int(input("Enter the second number "))

n=0
if a<b:
    i=a
else:
    i=b

while i>1:
    if a%i==0 and b%i==0:
        n=1
    i-=1
if n==0:
    print("%d and %d are co-prime"%(a,b))
else:
    print("%d and %d are not a co-prime"%(a,b))

#8.write a python script to print first N terms of a fibonacci series.

a=int(input("Enter the number "))
p=-1
q=1
i=1
r=0
while i<=10:
    r=p+q
    p=q
    q=r
    print(r,end=' ')
    i+=1

#9.write a python script to calculate LCM of two numbers.

a=int(input("Enter the number "))
b=int(input("Enter the second number "))

if a>b:
    i=a
else:
    i=b

while i<=a*b:
    if i%a==0 and i%b==0:
        break
    i+=1

print("%d and %d are LCM is "%(a,b),i)

#10.write a python script to calculate HCF of two numbers.

a=int(input("Enter the number "))
b=int(input("Enter the second number "))

if a<b:
    i=a
else:
    i=b

while i>=1:
    if a%i==0 and b%i==0:
        break
    i-=1

print("%d and %d are HCF is "%(a,b),i)