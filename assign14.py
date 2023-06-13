'''1. Write a Python script to create a list
of first N natural numbers.'''

a=int(input("Enter how many natural number you print"))

i=1
b=list()
while i<=a:
    b.append(i)
    i+=1
print(b)

'''2. Write a Python script to create a list of first N odd 
natural numbers'''

a=int(input("Enter how many natural number you print"))
i=1
b=list()
while i<=a:
    b.append(i*2-1)
    i+=1
print(b)

'''3. Write a Python script to create a list of first N 
even natural numbers'''

a=int(input("Enter how many natural number you print"))
i=1
b=list()
while i<=a:
    b.append(i*2)
    i+=1
print(b)

'''4. Write a Python script to find the greatest number in
a given list of numbers'''

a=eval(input("Enter list of value like [23,22,45] this "))
print(max(a))

'''
i=1
b=list()
print("Enter value")
while i<=5:
    b.append(int(input()))
    i+=1
print(max(b))
'''

'''5. Write a Python script to find the smallest number in a 
given list of numbers.'''

a=eval(input("Enter list of value like [23,22,45] this "))
print(min(a))

'''
i=1
b=list()
print("Enter value")
while i<=5:
    b.append(int(input()))
    i+=1
print(min(b))
'''

'''6. Write a Python script to calculate the sum of elements in 
a given list of numbers'''

a=eval(input("Enter list of value like [23,22,45] this "))
sum(a)

'''
i=1
b=list()
print("Enter value")
while i<=5:
    b.append(int(input()))
    i+=1
print(min(b))
'''

'''7. Write a Python script to remove all non int 
values from a list'''

b=[23,"yadav",3.5,45,73,True]
f=list()
for e in b:
    if type(e)==int:
        f.append(e)
print(f,end=' ')

'''8. Write a Python script to print distinct elements along with their frequencies of
occurrence in the list'''

i=1
b=list()
a=int(input(("Enter size of list ")))
while i<=a:
    b.append(int(input()))
    i+=1
while i<=a:
    s=b.count(i)
    print("%d is %d times"%(b[i],s))
    i+=1

'''9. Write a Python script to print indices
 of all occurrences of a given element in
a given list.'''

i=1
b=list()
a=int(input(("Enter size of list ")))
while i<=a:
    b.append(int(input()))
    i+=1

for e in b:
    print(b.index(e))

#10. Write a python script to sort a list.

i=1
b=list()
a=int(input(("Enter size of list ")))
while i<=a:
    b.append(int(input()))
    i+=1
print(sorted(b))