#1.write a python script to calculate sum of first N natural numbers.

i=int(input("Enter the number "))
n=1
s=0
while n<=i:
    s=s+n
    n+=1
print(s,end=' ')

#2.write a python script to calculate sum of aquares of first N natural numbers.

i=int(input("Enter the number "))
n=1
s=0
while n<=i:
    s=s+n**2
    n+=1
print(s,end=' ')

#3.write a python script to calculate sum of cubes of first N natural numbers.

i=int(input("Enter the number "))
n=1
s=0
while n<=i:
    s=s+n**3
    n+=1
print(s,end=' ')

#4.write a python script to calculate sum of first N odd natural nubers.

i=int(input("Enter the number "))
n=1
s=0
while n<=i:
    s=s+(2*n-1)
    n+=1
print(s,end=' ')

#5.write a python script to calculate sum of first N even natural numbers.

i=int(input("Enter the number "))
n=1
s=0
while n<=i:
    s=s+(2*n)
    n+=1
print(s,end=' ')

#6.write a python script to calculate factorial of a given number.

i=int(input("Enter the number "))
s=1
while i>0:
    s=s*i
    i-=1
print(s,end=' ')

#7.write a python script to count digit in given number.

i=int(input("Enter the number "))
n=0
while i>0:
    if i>0:
        i=i/10
        n+=1
print("Number of digit is ",n)

#8.write a python script to calculate sum of digits of a given number.

i=int(input("Enter the number "))
sum=0
while i>0:
    if i>0:
        s=i%10
        sum=sum+s
        i=i/10
print("sum of digit is ",sum)

#9.write a python script to print binary equivalent of a given
#decimal number.(do not use bin()method)

i=int(input("Enter decimal number "))
while i>0:
    s=i%2
    print(s,end=' ')
    i=int(i/2)

