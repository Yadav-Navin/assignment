
'''1) write a python script to display the number of days in a
given month number.'''

day=int(input("Enter the number "))
match day:
    case 4:
        print("30 days")
    case 6:
        print("30 days")
    case 9:
        print("30 days")
    case 11:
        print("30 days")
    case 4,6,9,11:
        print("30 days")
    case 1:
        print("31 days")
    case 3:
        print("31 days")
    case 5:
        print("31 days")
    case 7:
        print("31 days")
    case 8:
        print("31 days")
    case 10:
        print("31 days")
    case 12:
        print("31 days")
    case 2:
        print("28 or 29 days")
    case _:
        print("Invalid month")

'''2) write a menu driven program to perform following operation
Addition ,subtraction ,Multiplication ,division.'''

print("1.Addition")
print("2.Subtraction")
print("3.Division")
print("4.Multiplication")
print()
inp=int(input("choose a number "))
match inp:
    case 1:
        no1=int(input("Enter the first number "))    
        no2=int(input("Enter the second number "))
        s=no1+no2
        print("Addition is",s)
    case 2:
        no1=int(input("Enter the first number "))    
        no2=int(input("Enter the second number "))
        s=no1-no2
        print("Subtraction is",s)
    case 3:   
        no1=int(input("Enter the first number "))    
        no2=int(input("Enter the second number "))
        s=no1/no2
        print("Division is",s)
    case 4:
        no1=int(input("Enter the first number "))    
        no2=int(input("Enter the second number "))
        s=no1*no2
        print("Multiplication is",s)
    case _:
        print("Invalid choice")

'''3) write  a menu driven program with the following options:'''

print("1.Check whether a given set of three number are lenghts of an isosceles triangle or not.")
print("2.Check whether a given set of three numbers are lengths og sides of a right angled triangle or not")
print("3.Check whether a given set of three numbers are equilateral triangle or not")
print("4.Exit")
i=int(input("Choose the number "))


'''4)write a program which takes user's age and display the category
of person .Age below 10 years -kid,age below  2o -teen ,age below 40-young
age below 60-experienced,age above or equal 60-senior citizen.'''

age=int(input("Enter the age "))
if age<=10:
    a1=1
elif 10<age<=20:
    a1=2
elif 20<=age<=40:
    a1=3
elif 40<=age<=60:
    a1=4
else:
    a1=5
match a1:
    case 1:
        print("kids")
    case 2:
        print("Teen")
    case 3:
        print("Young")
    case 4:
        print("Experianced")
    case 5:
        print("Seniour citizen")


'''5)write a program which takes a number from the user.print Saurabh
Shukla if the number is even ,print prateek jain if the number is
nagative odd number and print aditya if number is positive odd.'''

in1=int(input("Enter the number "))
if in1<0:
    if in1%2!=0:
        n=-1
if in1>0:
    if in1%2==0:
        n=2
    elif in1%2!=0:
        n=1
    else:
        n=0

match n:
    case 2:
        print("Saurabh Shukla")
    case 1:
        print("Aditya")
    case -1:
        print("Prateek")
    case _:
        print("invalid")
    
'''6) write a python program to check whether a given string is a 
multiword string or single word using match case statement.'''

st=str(input("Enter the string "))

if st!=' ':
    n=1
else:
    n=2

match n:
    case 1:
        print("Multiword string")
    case 2:
        print("Single word")

'''7) write a python program to check whether a given number is
positive ,negative or zero using match case statement.'''

nu=int(input("Enter the number "))
if nu>0:
    n=1
elif nu<0:
    n=2
else:
    n=3

match n:
    case 1:
        print("Positive")
    case 2:
        print("Negative")
    case 3:
        print("zero")

'''8) write a python script to check whether two given strings are identical
first string comes before the second in dictionary order or first sting
comes after the second string in dictionary order using match case statement.'''

st=str(input("Enter the string "))
st1=str(input("Enter the second string "))

if st==st1:
    n=1
if st1>st:
    n=3
else:
    n=4

match n:
    case 1:
        print("Identical")
    case 3:
        print(st,st1)
    case 4:
        print(st1,st)

'''9) write a python script to check whether a given year is 
a.Non century leap year
b.Century leap year
c.Non century non leap year
d.Century non leap year
'''
a=int(input("Enter the year "))
if a%4==0:
    n=1
elif a%400==0:
    n=2
elif a%4!=0:
    n=3
else:
    n=4


'''10) write a program to display day name on the basis of user's liking
of a colour.Ask user for his favorite colour.User can answer in a sentence
like "i like red colour". Assuming all colour name entered by user is in
lowercase .Use match case to display day name associated with the colour'''

'''
Yellow-Monday
Blue-Tuesday
orange-Wendnesday
White-Thursday
Black-Friday
All other colours-Sunday
'''
print("\"i like red color\" enter like this ")
st=str(input("Enter your favorite colour "))

match st:
    case "i like yellow colour":
        print("Monday")
    case "i like blue colour":
        print("Tuesday")
    case "i like orange colour":
        print("Wednesday")
    case "i like white colour":
        print("Thursday")
    case "i like black colour":
        print("Friday")
    case "i like red colour":
        print("Saturday")
    case _:
        print("Sunday")
