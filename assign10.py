#1) write a python script to print the first 10 multiples of 5.

a=range(5,10*5+5,5)
j=1
for i in a:
    print("5 * %d ="%j,i)
    j+=1

#2) write a python script to print first 10 multiples of N.

i=int(input("Enter the number "))
a=range(i,i*10+i,i)
l=1
for k in a:
    print("%d * %d ="%(i,l),k)
    l+=1

#3) write a python script ti print the first M multiples of N.

i=int(input("Enter the number "))
ra=int(input("Enter how many times multiples "))
a=range(i,i*ra+i,i)
l=1
for k in a:
    print("%d * %d ="%(i,l),k)
    l+=1

#4) write a python script to print the first 10 multiples of N in reverse order.

i=int(input("Enter the number "))
a=range(i*10,0,-i)#end exclusive hota hai tha's why we can not write i insted of 0.
l=10# step difference is -i.
for k in a:
    print("%d * %d ="%(i,l),k)
    l-=1

#5) write a python script to print table of user's choice.

i=int(input("Enter the table number "))
a=range(i,i*10+i,i)
l=1
for k in a:
    print("%d * %d ="%(i,l),k)
    l+=1

#6) write a python script to print first N even natural numbers.

i=int(input("Enter first N even number "))
j=1
while j<=i:
    print(2*j,end=' ')
    j+=1

#7)write a python script to print first N odd natural numbers.

i=int(input("Enter first N odd number "))
j=1
while j<=i:
    print(2*j-1,end=' ')
    j+=1

#8)write a python script to print square of fist N natural numbes.

i=int(input("Enter first N square number "))
j=1
while j<=i:
    print(j**2,end=' ')
    j+=1

#9) write a python script to print cubes of first N natural numbers.

i=int(input("Enter first N cubes number "))
j=1
while j<=i:
    print(j**3,end=' ')
    j+=1

#10) write a python script to display all prime numbers within a range.
#range start = 15  end = 45

r=range(15,45)
for a in r:
    i=2
    n=0
    while i>1 and i<a:
        if a%i==0:
            n=1
        i+=1
    if n==0:
        print(a,end=' ')
