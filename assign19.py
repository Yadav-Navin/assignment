'''1. Write a python program to create a simple function which prints “MySirG” .
'''

def f1():
    print("MysirG")
f1()

'''2. Write a python program to create a function which expects two arguments and print
them in the function body.'''

def f2(a,b):
    print("a={} and b={}".format(a,b))
f2(4,5)

'''3. Write a python program to create a function which expects an unknown number of
arguments.
'''

def f3(*t):
    a=sum(t)/len(t)
    print(a)
f3(10,20,30)
f3(50,40)

'''4. Write a python program to create a function which expects kwargs arguments'''

def f4(a,b):
    print("a={}and b={}".format(a,b))

f4(b=4,a=4)
f4(4,5)

'''5. Write a python program to create a function which expects a list as an argument'''

def f5(l1):
    print(l1)
f5(l1=[45,54,66,89])#we are pass keyword argument throught list


'''6. Write a python program to create a function that finds a maximum of four numbers.
'''

def f6(*t):
   print(max(t))

    # if a>b and b>c and b>d:
    #     print(a)
    # elif b>c and c>d and c>a:
    #     print(b)
    # elif c>d and d>b and d>a:
    #     print(c)
    # else:
    #     print(d)
f6(34,20,45,55,10,56,28)   

'''7. Write a python program to sum all the numbers in a list.
'''

def f7(l1):
    print(sum(l1))
f7(l1=[10,20,30,40,50])

'''8. Write a python program to multiply all the numbers in a list'''

def f8(l1):
    s=1
    for e in l1:
        s=s*e
    print("multiply of list is ",s)
f8(l1=[10,20,30])

'''9. Write a python program to create a function to check whether a number falls in a
given range.
'''

    
    

'''10. Write a python program to create a function to check whether a given number is even
or odd.'''

def f10(n):
    print("Odd" if n%2 else "Even")
f10(10)
