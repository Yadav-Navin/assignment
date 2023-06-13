'''1. Write a recursive python function to print first N natural numbers.
'''

def first_natural_no(n):
    if n>0:
        first_natural_no(n-1)
        print(n)
        
first_natural_no(5)

'''.2. Write a recursive python function to print first N natural numbers in reverse order
'''

def f2(n):
    if n>0:
        print(n)
        f2(n-1)

f2(5)

'''3. Write a recursive python function to print first N odd natural numbers
'''

def f3(n):
    if n>0:
        f3(n-1)
        print(2*n-1)
    
f3(10)

'''4. Write a recursive python function to print first N odd natural numbers in reverse order'''

def f4(n):
    if n>0:
        print(2*n-1)
        f4(n-1)

f4(10)

'''5. Write a recursive python function to print first N even natural numbers.'''

def f5(n):
    if n>0:
        f5(n-1)
        print(2*n)

f5(5)

'''6. Write a recursive python function to print first N even natural numbers in reverse
order'''

def f6(n):
    if n>0:
        print(2*n)
        f6(n-1)

f6(5)

'''7. Write a recursive python function to print squares of first N natural numbers'''

def f7(n):
    if n>0:
        f6(n-1)
        print(n**2)
        
f7(5)

'''8. Write a recursive python function to print cubes of first N natural numbers
'''

def f8(n):
    if n>0:
        f6(n-1)
        print(n**3)
        
f8(5)

'''9. Write a recursive python function to print first N multiples of a given number.
'''

def f8(n,m):
    if m>0:
        f8(n,m-1)
        print("{} * {} = {}".format(n,m,n*m))

f8(5,10)

'''10. Write a recursive python function to print a number in reverse order'''

def f10(n):
    if n:
        print(n%10)
        f10(int(n/10))
    
f10(2345)



