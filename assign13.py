'''1.write a python script to store multiple items
in a single variable(item are "java","python"
"SQL","C")using list.'''

a=["Java","Python","SQL","C"]

'''2.Write a python script to get the
data type of a list.'''

print("Enter list type value like this [12,23,33]")

a=eval(input())

'''3. Write a python script to get the last item 
of the list ( mylist = ["Java", "C", "Python"])'''

mylist = ["Java", "C", "Python"]
print(mylist[-1])

'''4. Write a python script to Change the values "SQL" and "Reactnative" with the values
"NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative",
"Javascript", "Python"]'''

List = ["Java", "SQL", "C", "Reactnative",
"Javascript", "Python"]
List[1]="NoSQL"
List[3]="Flutter"

print(List)

'''5. Write a python script to add an item to the end of the list (item “Python”. (mylist =
["Java", "SQL", "C", "Reactnative"]'''

mylist =["Java", "SQL", "C", "Reactnative"]

mylist.append("Python")
print(mylist)

'''6. Write a python program to append elements from another list to the current list.(
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"] )'''

firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]

for e in secondlist:
    firstlist.append(e)
print(firstlist)
    
'''7. Write a python program to Print all items by referring to their index number (thislist =
["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]'''

thislist =["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
i=0
while i<len(thislist):
    print(thislist[i])

'''8. Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL",
"C", "Reactjs", "Javascript", "Python"]'''

thislist = ["Java", "SQL",
"C", "Reactjs", "Javascript", "Python"]
thislist.sort()
print(thislist)

'''9. Write a Python script to create a list of city names taken from the user'''

a=eval(input("Enter the city list like this [surat,Nadiad]"))
print(a)

'''
a=list()
i=0
while i<5:
    b=input()
    a.append(b)
    i+=1
print(a)
'''

'''10. Write a Python script to create a list, where each element of the list is a digit of a
given number.'''

n=int(input("Enter list size "))
a=list()
i=0
print("Enter only digit")
while i<n:
    b=input()
    a.append(b)
    i+=1
print(a)

'''
a=eval(input("Enter the city list like this [surat,Nadiad]"))
print(a)
'''
