'''1. Write a python program to store all the programming languages known to you using
Set.
'''

a={"C","Java","Python","HTML","CSS","Javascript"}
print(a)

'''2. Write a python program to store your own information {name, age, gender, so on..}'''

print("Enter your name ,age,gender,separeted by comma")
a=input()
s={e for e in a.split(',')}
print(s)

'''3. Write a python script to get the data type of a Set.
'''

print("Enter anyone separeted by comma")
a=input()
s={e for e in a.split(',')}
print(type(s))

'''4. Write a Python script to find if “Python” is present in the set thisset = {"Java",
"Python", "Django"}'''

thisset = {"Java","Python", "Django"}
print("Yes" if "Python" in thisset else "No")

'''5. Write a python program to add items from another set to the current set. thisset =
{"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
'''

thisset ={"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}

for e in secondset:
    thisset.add(e)
print(thisset)

'''6. Write a python program to add elements of list to a set
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
'''

thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
thisset.app(mylist)
print(thisset)

'''7. Write a python program to remove last item of the given set
thisset = {"Python", "Django", "JavaScript", “SQL”}
'''

thisset = {"Python", "Django", "JavaScript", "SQL"}
thisset.discard("SQL")
print(thisset)

'''8. Write a python program to delete the set completely.
'''

thisset = {"Python", "Django", "JavaScript", "SQL"}
del thisset

'''9. Write a python program to loop through the set and print values
'''

thisset = {"Python", "Django", "JavaScript", "SQL"}
for e in thisset:
    print(e)

'''10. Write a python program to find the maximum and minimum value in a set.'''

print("Enter the number separeted by comma")
a=input()
l={int(e) for e in a.split(',')}
print(l)
print(max(l))






