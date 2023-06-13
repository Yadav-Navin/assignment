'''1) write a python script to check whether a given number is
positive or non-positive.'''

po=int(input("Enter the number "))
if po>0:
    print("Positive")
else:   
    print("Non-positive")

'''2) write a python script to check whether a given number is
divisible by 5 or not.'''

num=int(input("Enter the number "))
if num%5:
    print("Not divisible by 5")
else:
    print("Number is divisible by 5")

'''3) write a python script to whether a given number is even
or odd.'''

num1=int(input("Enter the number "))
if num1%2:
    print("Odd")
else:
    print("Even")
    
'''4) write a python script to print greater between two numbers.
Print number only once even if the numbers are the same.'''

num2=int(input("Enter the number "))
num3=int(input("Enter the second number "))
if num2>num3:
    print("Number %d is greater then %d"%(num2,num3))
elif num3>num2:
    print("Number %d is greater then %d"%(num3,num2))
else:
    print("%d and %d are the same"%(num2,num3))

'''5) write a python script to print two given words in dictionary
order.'''

str1=input("Enter the first word ")
str2=input("Enter the second word ")
if str1<str2:
    print("%s and %s"%(str1,str2))
else:
    print("%s and %s"%(str2,str1))

'''6) write a ptyhon script to check whether a given number is
a three digit number or not.'''

digit=int(input("Enter the number "))
if 100<=digit<=999:
    print("Number is three digit")
else:
    print("Not a three digit")


'''7) write a python script to check whether a given number is
positive,negative or zero.'''

po=int(input("Enter the number "))
if po>0:
    print("Positive")
elif po<0:
    print("Negative")
else:
    print("zero")

'''8) write a python script to check whether a given quadratic
equation has two real & distinct roots,teal & wquzl roots or
imaginary roots.'''

print("Quadratic equation like 5x*x-6x+5=0 here x*x base 5 just kike this")
img1=int(input("Enter the a number "))
img2=int(input("Enter the b value "))
img3=int(input("Enter the c value "))
qu=(-img2+(img2-2*img1*img1*img3*img3))/2*img1
qu1=(-img2-(img2-2*img1*img1*img3*img3))/2*img1
root=img2*img2-4*img1*img3
if root>0:
    print("Real & disctint")
elif root<0:
    print("imaginary")
else:
    print("equal roots")

'''9) write a python script ro check whether a given year is leap
or not.'''

ye=int(input("Enter the year "))
if ye%400==0:
    print("leap year")
elif ye%100==0:
    print("not leap year")
elif ye%4==0:
    print("leap year")
else:
    print("not leap year")

'''10) write a python script to print grater among three numbers.
print number only once even if the numbers are the same.'''

a1=int(input("Enter the first number "))
a2=int(input("Enter the second number "))
a3=int(input("Enter the third number "))
if a2<a1>a3:
    print("Number %d is greater"%a1)
elif a1<a2>a3:
    print("Number %d is greater"%a2)
elif a1<a3>a2:
    print("Number %d is greater"%a3)
else:
    print("all number should be same %d"%a1)

'''11) write a python script to take the month value in numeric
format and display the number of days in it.'''

day=int(input("Enter the month number "))
if 4 or 6 or 9 or 11:
    print("30 days")
elif 2:
    print("28 or 29 days")
else:
    print("31 days")

'''12) write a python script to accept one complex number from
the user and display the greater number between real part and
imaginary part.'''

com=complex(input("Enter the complex number "))
if com.real>com.imag:
    print(com.real)
else:
    print(com.imag)
