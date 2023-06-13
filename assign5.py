'''1) write a python script to remove the last digit from a given 
a number .(for example ,if user enters 2534 then your output should 
be 253)'''

a=int(print("Enter the number "))
remove=a/10
print("Your number is ",remove)

'''2) write a python script to get the last digit from a given number.
(for example ,if user enters 2098 then your output should be 9)'''

lastdigit=int(input("Enter the number "))
lastdigit1=lastdigit%10
print("Last digit is ",lastdigit1)

'''3) write a python script to swap data of two variables'''

firstdata=int(input("Enter first data "))
seconddata=int(input("Enter the second data "))
thirddata=firstdata
firstdata=seconddata
seconddata=thirddata
print("change data firstdata is %d and seconddata is %d"%(firstdata,seconddata))

'''4) write a python script to find x power of y ,where values of
x and y are given by user.'''

power=int(input("Enter the number of x is "))
power1=int(input("Enter the x power of y "))
power3=power**power1 #we are use exponential operator
print("Power of %d is %d"%(power,power3))

'''5) write a python script which takes a three digit number from the 
user and displays only it's first digit.'''

threedigit=int(input("Enter the three digit number only "))
threedigit1=threedigit/100
print("Your is %d and his first digit is %d"%(threedigit,threedigit1))

'''6) write a python script which takes a three digit number form the
user and display only its last digit.'''

last=int(input("Enter the only three digit number "))
last1=last%10
print("Value is %d  and it's last digit is %d"%(last,last1))

'''7) write a python script which takes a three digit number form the
user and display only it's middle digit.'''

middle=int(input("Enter the only three digit number "))
middle1=middle%100
print("Value is %d and it's middle digit is %d"%(middle,middle1))

'''8) write a python script to use IN operator to display the data present
in the list.'''

oper=input("Enter the string ")
oper1=input("Enter the any character or word ")
print(oper1 in oper)

'''9)write a python scipt to use NOT IN operator to display the data
not present in list.'''

str1=input("Enter the string ")
str2=input("Enter the any character or word ")
print(str2 not in str1)

'''10) write a python script to use IS operator to display if both 
variables are the same object or not? '''

v1=int(input("Enter the first number "))
v2=int(input("Enter the second number "))
print(v2 is v1)
