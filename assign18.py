'''1. Write a python program to create and print a dictionary which stores your information.
(name, age, gender …..)'''

n=input("Enter your name ")
a=int(input("Enter your age "))
g=input("Enter the gender ")

di=dict(name=n,age=a,gender=g)
print(di)

'''2. Write a python program to access the items of a dictionary by referring to its key
name.
'''

n=input("Enter your name ")
a=int(input("Enter your age "))
g=input("Enter the gender ")

di=dict(name=n,age=a,gender=g)
print(di["name"])

'''3. Write a python program to get a list of the values from a dictionary.
'''

d={102:'Rahul',105:'Amit',106:'Navin',108:'Saurabh'}
print(d.values())

'''4. Write a python program to change the value of a specific item by referring to its key
name'''


d={102:'Rahul',105:'Amit',106:'Navin',108:'Saurabh'}
d[105]='Darmesh'
print(d.items())

'''5. Write a python program to print all key names in the dictionary, one by one.
'''

d={102:'Rahul',105:'Amit',106:'Navin',108:'Saurabh'}
print(d.keys())

'''6. Write a python program to create a dictionary that contains three dictionaries.
(nested)
'''

a={102:'Rahul',105:'Amit'}
b={106:'Navin',108:'Saurabh'}
c={205:'Ravi',206:'Mahesh'}
d={}

d[0]=a.copy()
d[1]=b.copy()
d[2]=c.copy()
print(d)

d={{102:'Rahul',105:'Amit'},{106:'Navin',108:'Saurabh'},{205:'Ravi',206:'Mahesh'}}
print(d)

'''7. Write a python program to create three dictionaries, then create one dictionary that
will contain the other three dictionaries.
'''

a={102:'Rahul',105:'Amit'}
b={106:'Navin',108:'Saurabh'}
c={205:'Ravi',206:'Mahesh'}
d={}

d[0]=a.copy()
d[1]=b.copy()
d[2]=c.copy()
print(d)

'''8. Write a python program to convert two lists into a dictionary in a way that item from
list1 is the key and item from list2 is the value.
'''

list1=[193,194,195,196,197]
list2=['Navin','Ravi','Ramesh','saurabh','Rohit']
a=dict(list1=list2)
print(a)

'''9.write a python program to merge two python dictionaries into one dictionary.
'''

a={102:'Rahul',105:'Amit'}
b={106:'Navin',108:'Saurabh'}
a.update(b)
print(a)


'''10. Write a python program to get the key of lowest value from the dictionary.
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}'''

sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}
print(min(sample_dict.values()))


