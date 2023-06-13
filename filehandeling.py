'''
1. Write a Python script to print the following status of a file:
a. Whether a file is read only
b. Whether a file is closed or not
c. Which file opening mode is used
d. Name of the file'''

def file(filename,string):
    try:
        f = open(filename,'w')
        f.write(string)
    except FileNotFoundError:
        print("File not found")
    finally:
        f.close()
    
s = input("Enter the string : ")    
file('file.txt',s)


'''
2. Write a Python script to create a new file ‘myfile.txt’ and store user entered text.'''


def file1(filename,string):
    try:
        f = open(filename,'w')
        f.write(string)
    except FileNotFoundError:
        print("File not found")
    finally:
        f.close()
    
s = input("Enter the string : ")    
file1('myfile.txt',s)



'''3. Write a Python script to read the above created file ‘myfile.txt’ and display content on
the console.'''

def file1(filename):
    try:
        f = open(filename,'r')
        print(f.read())
    except FileNotFoundError:
        print("File not found")
    finally:
        f.close()
  
file1('myfile.txt')


'''4. Write a Python script to store a list of city names in a file ‘cities.txt’'''

def store():
    a = """Nadiad,Surat,Jaunpur,Ahmedabad,Dakor,Bhuj"""
    try:
        f = open('cities.txt','w')
        f.write(a)
    except FileNotFoundError:
        print("file not found")
    finally:
        f.close()
    
store()

'''5. Write a Python script to append list of city names in a file ‘cities.txt’'''

def store1():
    a = '''chitagong,Mumbai,Lacknow,Dahod,Godhara,valsad''' 
    try:
        f = open('cities.txt','a')
        f.write(a)
    except FileNotFoundError:
        print("file not found")
    finally:
        f.close()
  
store1()

'''6. Write a Python script to search whether a particular city is there in the file ‘cities.txt’ or
not'''

def search(filename,word):
    try:
        f = open(filename,'r')
        a = f.readline()
        a = a.split(',')
        return(word in a)
    except FileNotFoundError:
        print("File not found")
    finally:        
        f.close()
search('cities.txt','Bhuj')


'''7. Write a Python script to count the number of Python keywords occurring in a python
source file.
8. Write a Python script to create a copy of a file.
9. Write a Python script to store book data in a file. Book data is in the form of a
dictionary in which book name is the key and price is its value. Use pickle to store
data into a file (say bookfile)
10. Write a Python script to extract book data from a bookfile using pickle. Also print
extracted book data.
'''