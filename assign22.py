#1. Write a recursive python function to calculate sum of first N natural numbers

def  f1(n):
    if n==1:
        return 1
    return n+f1(n-1)

a=f1(5)
print(a)

#2. Write a recursive python function to calculate sum of first N odd natural numbers

def f2(n):
    if n==0:
        return 0
    s=2*n-1+f2(n-1)
    return s

b=f2(3)
print(b)

#3. Write a recursive python function to calculate sum of first N even natural numbers

def f3(n):
    if n==0:
        return 0
    s=2*n+f3(n-1)
    return s

b=f3(3)
print(b)

#4. Write a recursive python function to calculate sum of squares of first N natural
#numbers

def f4(n):
    if n==0:
        return 0
    s=n**2+f4(n-1)
    return s

b=f4(3)
print(b)

#5. Write a recursive python function to calculate sum of cubes of first N natural
#numbers

def f5(n):
    if n==0:
        return 0
    s=n**3+f5(n-1)
    return s

b=f5(3)
print(b)

#6. Write a recursive python function to calculate the factorial of a number.

def f6(n):
    if n==0:
        return 1
    s=n*f6(n-1)
    return s

b=f6(3)
print(b)

#7. Write a recursive python function to calculate sum of the digits of a given number

def f7(n):
    if n==0:
        return 0
    return n%10+f7(int(n/10))

a=f7(523)
print(a)

#8. Write a recursive python function to print binary of a given decimal number

def f8(n):
    if n==0:
        return 0
    f8(int(n/2))
    print(n%2,end='')
    #bin(n)

f8(10)

#9. Write a recursive python function to print octal of a given decimal number

def f8(n):
    return oct(n)

a=f8(int(input("Enter decimal ")))

