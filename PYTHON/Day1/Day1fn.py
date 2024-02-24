Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 21:52:07) [MSC v.1937 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a =10
b = a
print(a is b)
True
if 3<7:
    print("hi")

    
hi
if 3:
    print("hi")

    
hi
if -45:
    print("hi")

    
hi
if 0:
    print("hi")

    
>>> a = int(input())
if a:
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a = int(input())
ValueError: invalid literal for int() with base 10: 'if a:'
>>> if a :
...     print("hi")
... 
...     
hi
>>> a = int(input("Enter a number"))
Enter a number3
>>> if a :
...     print("hi")
... 
...     
hi
>>> a = int(input("Enter a number"))
Enter a number7
>>> if a :
...     print("hi")
... else :
...     print("bye")
... 
...     
hi
>>> a=int(input("enter the radius of circle"))
enter the radius of circle2
>>> b=int(input("enter the length of the rectangle"))
enter the length of the rectangle
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    b=int(input("enter the length of the rectangle"))
ValueError: invalid literal for int() with base 10: ''
>>> b=int(input("enter the length"))
enter the length2
>>> c=int(input("enter the breadth"))
enter the breadth3
>>> area=b*c
>>> print(area)
6
>>> area=3.14*(a*2)
>>> 
>>> print (area)
12.56
