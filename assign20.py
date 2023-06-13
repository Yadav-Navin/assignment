'''1. Write a python program to create a function that takes a list and returns a new list
with the original list's unique elements.'''

def f1(l):
    l1=set(l)
    l=list(l1.union(l1))
    return l
print(f1(l=[23,90,23,90,5]))

'''2. Write a python program to create a function that takes a number as a parameter and
checks if the number is prime or not.'''

def f2(a):
    i=2
    while i<a:
        if a%i==0:
            print("Not a prime")
            break
        i+=1
    else:
        print('prime')
f2(7)

'''3. Write a python program to create a function that prints the even numbers from a
given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

def f3(List):
    print([e for e in List if e%2==0])

f3(List = [1, 2, 3, 4, 5, 6, 7, 8, 9])

'''4. Write a python program to create a function that checks whether a passed string is
palindrome or not.
'''

def f4(a):
    b=a[::-1]
    print("Palindrom" if a==b else "Not palindrom")

f4(input("Enter the palindrom string "))

'''5. Write a python program to create a function to find the Min of three numbers.
'''

def f5(*t):
    print(min(t))

f5(23,56,20)

'''6. Write a python program to create a function and print a list where the values are
square of numbers between 1 and 30.
'''

def f6():
    print("Square of number between 1 to 30")
    print([e**2 for e in range(1,30)])
f6()

'''7. Write a python program to access a function inside a function.
'''

def f7(n):
    if n==1:
        return 1
    return n+f7(n-1)
print(f7(5))

'''8. Write a python program to create a function that accepts a string and calculate the
number of upper case letters and lower case letters.
'''

def f8(a):
    n=0
    i=0
    for e in a:
        if e>='A' and e<='Z':
            n+=1
        if e>='a' and e<='z':
            i+=1
    print("Capital latter is ",n)
    print("Lower case is ",i)
f8(input("Enter the string "))

'''9. Write a python program to create a function to check whether a string is a pangram
or not.'''

def f9(a):
    b=set()
    for e in a:
        if e>='a' and e<='z':
            b.add(e)
        if e>='A' and e<='Z':
            e=e.lower()
            b.add(e)
    return len(b)==26

if f9(input("Enter the string to check pangram "))==True:
    print("pangram string")
else :
    print("not pangram string")


'''9. Write a python program to create a function to check whether a string is a anagram
or not.'''

def f10(s,s1):
    a=set(s)
    b=set(s1)
    print("Anagram" if a==b else "Not anagram")

f10(input("Enter first string "),input("Enter second string "))






            





