'''1. Write a python script to create a String 
in 3 different possible ways'''

a="Navin Yadav"
b='Saurabh Yadav'
c="""Jay bajarang bali"""
d='''Jay shree ram'''

'''2. Write a python script to Get the characters from the start to position 5 (Given String
“iNeuron” using the slice syntax)
'''

a="iNeuron"
print(a[5::1])

'''3. Write a python script to Get the characters from position 2 to position 5 (Given String
“Hello Learners” using the slice syntax)'''

a="Hello Learners"
print(a[2:5:1])

'''4. Write a python script to demonstrate String Concatenation adding space in between (
Given Strings a=”Learning” b=”Python” )
'''

a="Learning"
b="Python"
print(a+' '+b)

li=list()
li.append(a)
li.append(b)
print(' '.join(li))
print(li)

'''5. Write a python script to get the count
 of total number of characters in String a=
“iNeuron”'''

a=str(input("Enter the string "))
i=1
nu=0
for e in a:
    if (ord(e)>=65 and ord(e)<=90) or (ord(e)>=97 and ord(e)<=122):
        nu+=1
print("Total number of character is %d"%nu)


'''6. Write a python script to reverse a String. (“iNeuron”)'''

a="iNeuron"
print(a[::-1])

'''7. Write a python script to determine whether a string contains a specific substring.
'''

a=str(input("Enter the string "))
b=str(input("which string you want to search enter here "))
print(b in a)

'''8. Write a python script to check if a string contains only numbers.
'''

a=str(input("Enetr the strung "))
print(a.isdigit())

'''9. Write a python script to check if a string contains only characters of the alphabet.
'''
a=str(input("Enetr the strung "))
print("check string cotains only alphabet")
print(a.isalpha())

'''10. Write a python script to convert an integer to a string.'''

a=int(input("Enter the number "))
print("converted string is here")
print(str(a))