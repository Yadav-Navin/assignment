'''1. Write a python script to store multiple items in a single variable ( Items are “Java”
,“Python”, “SQL”, “C” ) using tuple'''

a=("Java","Python","SQL","C")
print(a)
print(type(a))
b="Java","Python","SQL","C"
print(b)

'''2. Write a python program to store only one
 item using tuple.'''

i=input("enter the number ")
l=[eval(e) for e in i]
l=tuple(l)
print(l)

'''3. Write a python program to reverse the 
tuple.'''

print("Enter the number separeted by comma ")
a=input()
l=[eval(e) for e in a.split(',')]
l=tuple(l)
i=1
while i<=len(l):
    print(l[-i],end=' ')
    i+=1

'''4. Write a python program to Swap two 
tuples in Python.'''

a=(10,35,45,55)
b=(12,54,56,87)

f=tuple([e for e in b])
del b
b=tuple([e for e in a])
print(b)
del a
a=tuple([e for e in f])
print(a)

'''5. Write a python program to check if all 
items in the tuple are the same.'''

print("Enter the number separedted by comma")
l=input()
l=tuple(int(e) for e in l.split(','))
print(l)
i=1
nu=0
for e in l:
    if l[0]==e:
        nu+=1
print("All item is same in tuple" if nu==len(l) else "Not same")

'''6. Write a python program to divide the tuple into four variables.
tuple1=(100, 200, 300, 400)'''

tuple1=(100,200,300,400)
a,b,c,d=tuple1
print(a,b,c,d)

'''7. Write a python program to copy elements 
4 and 5 from the following tuple into a new
tuple. tuple1=(1,2,3,4,5,6)'''

tuple1=(1,2,3,4,5,6)
l=tuple(e for e in tuple1 if e==4 or e==5)
print(l)

'''8. Write a python program to Sort a tuple of 
tuples by the second item.
tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))'''

tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))  
l=list(tuple1)
i=0
j=0
k=list()
while i<len(l)-1:
    j=i+1
    while j<len(l):
        if l[i][1]>=l[j][1]:
            k.append(l[i])
            l[i]=l[j]
            l[j]=k[0]
            k.clear()
        j+=1
    i+=1
l=tuple(l)
print(l)

'''9. Write a python program to print the 
value 20 from given nested tuple
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))'''

tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
print(tuple1[1][1])

'''10. Write a python program to change the first item (22) of a list within the following tuple
to 222.
tuple1 = (11, [22, 33], 44, 55)'''


tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]=222
print(tuple1)