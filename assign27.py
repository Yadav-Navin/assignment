'''
1. Write a python script to create a ArithmeticError'''

def division():
    a = int(input("Enter the number "))
    b = int(input("Enter the second number "))
    if a==b:
        raise ArithmeticError()
    try:
        c=a/b
    except ZeroDivisionError:
        print("zero division Error")
    except ArithmeticError:
        print("value does not same")
    else:
        print("result is",c)
    
division()
'''    
2. Write a python script to create a ValueError'''

def value():
    
    try:
        a = int(input("Enter the number "))
        b = int(input("Enter the second nuber "))
        if a==str:
            raise ValueError()
        c= a/b
    except ValueError:#handle wrong input
        print("value me problem hai baba")
    except ZeroDivisionError:
        print("Value is not divisible by zero")
    else:
        print("value is",c)

value()

'''
3. Write a python script to handle the ArithmeticError'''

def division1():
    a = int(input("Enter the number "))
    b = int(input("Enter the second number "))

    try:
        c=a/b
    except ZeroDivisionError:
        print("zero division Error")
    except ValueError:
        print("value must be number only..")
    else:
        print("result is",c)
    
division1()

'''
4. Write a python script to handle a ValueError'''

def value1():
    a = int(input("Enter the number "))
    b = int(input("Enter the second number "))

    try:
        c=a/b
    except ZeroDivisionError:
        print("zero division Error")
    except ValueError:
        print("value must be number")
    else:
        print("result is",c)
    
value1()

'''
5. Write a python script to handle multiple Exception in one try'''

def mul():
    a = int(input("Enter the number "))
    b = int(input("Enter the second number "))
    if a==b:
        raise ArithmeticError()
    try:
        c=a/b
    except ZeroDivisionError:
        print("zero division Error")
    except ArithmeticError:
        print("value does not same")
    except ValueError:
        print("value must be number")
    else:
        print("result is",c)
    
mul()

'''
6. Write a python script to create a calculator with 4 basic operations, and handle a
maximum number of exceptions.'''

class Calculator:

    def __init__(self):
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        ch = int(input("Choose the number "))
        if ch==1:
            self.addition()
        elif ch==2:
            self.sub()
        elif ch==3:
            self.mul()
        elif ch==4:
            self.div()
        else:
            print("Invalid choice")

    def addition(self):
        try:
            a = int(input("Enter the first number "))
            b = int(input("Enter the second number "))
            c = a + b
            print("Addition is",c)
        except ZeroDivisionError: 
            print("zero division Error")
        except ValueError:                   
            print("value must be numbers")
        except Exception:
            print("Unknown Error enter valid form")
            
    def sub(self):
        try:
            a = int(input("Enter the first number "))
            b = int(input("Enter the second number "))
            c = a - b
            print("Subtraction is",c)
        except ZeroDivisionError:
            print("zero division Error")
        except ValueError:
            print("value must be numbers")
        except Exception:
            print("Unknown Error enter valid form")
            
    def mul(self):
        try:
            a = int(input("Enter the first number "))
            b = int(input("Enter the second number "))
            c = a * b
            print("Multiplication is",c)
        except ZeroDivisionError:
            print("zero division Error")
        except ValueError:
            print("value must be numbers")
        except Exception:
            print("Unknown Error enter valid form")
            
    def div(self):
        try:
            a = int(input("Enter the first number "))
            b = int(input("Enter the second number "))
            c = a / b
            print("Division is",c)
        except ZeroDivisionError:
            print("zero division Error")
        except ValueError:
            print("value must be numbers")
        except Exception:
            print("Unknown Error enter valid form") 
            
c = Calculator()

        

'''
7. Write a python script to add a finally block for the above script'''

def check():
    try:
        a=10
        b=5
        c=a/b
        print(c)
    except ValueError:
        print("value error")
    except ZeroDivisionError:
        print("not divisible by zero")
    finally:
        print("finally executed....")
    




'''8. Write a python script to implement try except and else block for division'''

def else_check():
    
    try:
        a = int(input("Enter the number "))
        b = int(input("Enter the second nuber "))
        if a==str:
            raise ValueError()
        c= a/b
    except ValueError:#handle wrong input
        print("value me problem hai baba")
    except ZeroDivisionError:
        print("Value is not divisible by zero")
    else:
        print("value is",c)

else_check()

'''9. Write a python script to raise a ValueError.'''

def raise_check():
    
    try:
        a = int(input("Enter the number "))
        b = int(input("Enter the second nuber "))
        if a==str:
            raise ValueError()
        c= a/b
    except ValueError:#handle wrong input
        print("value me problem hai baba")
    except ZeroDivisionError:
        print("Value is not divisible by zero")
    else:
        print("value is",c)

raise_check()

'''10. Write a python script to implemented a nested Try Except block'''


        
            

        


