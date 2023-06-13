#1) write a python script to print MysirG N times onthe screen.

n=int(input("Enter the number "))
i=1
while i<=n:
    print("MysirG",end=' ')
    i+=1

#2) write a python script to print first N natural numbers.

n=int(input("Enter the number "))
i=1
while i<=n:
    print(i,end=' ')
    i+=1

#3) write a python script to print first N natural numbers in reverse order.

n=int(input("Enter the number "))
i=1
while i<=n:
    print(11-i,end=' ')
    i+=1

#4) write a python script to print first N odd natural numbers.

n=int(input("Enter the number "))
i=1
while i<=n*2:
    print(i,end=' ')
    i+=2

#5) write a python script to print first N odd natural numbers in reverse order.

n=int(input("Enter the number "))
i=n*2-1
while i>0:
    print(i,end=' ')
    i-=2
    
#6) write a pyton script to print first N even natural numbers.

n=int(input("Enter the number "))
i=2
while i<=n*2:
    print(i,end=' ')
    i+=2

#7) write a python script to print first N even natural numbers in reverse order.

n=int(input("Enter the number "))
i=n
while i>0:
    print(2*i,end=' ')
    i-=1

#8) write a python script to print square of first N natural number.

n=int(input("Enter the number "))
i=1
while i<=n:
    print(i**2,end=' ')
    i+=1

#9) write a python script to print cubes of first N natural numbers.

i=1
while i<=n:
    print(i**3,end=' ')
    i+=1

#10) write a python script to print first 10 multiple of N.

n=int(input("Enter the number "))
i=1
while i<=10:
    print("%d * %d ="%(n,i),i*n)
    i+=1

