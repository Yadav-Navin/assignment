print("Enter the number")
a=int(input())
print("Enter the second")
b=int(input())
print("******************")
if(a>b):
    i=a
else:
    i=b
while(i<a*b):
    if(i/a==0 & i/b==0):
        print("LCM:",i)
    i=i+1
