#1Python Program to Print Hello world!
"""
print ("Hello world!")

"""

#2 Python Program to Add Two Numbers
"""
a=6
b=4
k=a+b
print (k)
"""


#3 Python Program to Find the Square Root
"""
num=int(input("enter any number="))
print (num**2)
"""

#4 Python Program to Calculate the Area of a Triangle
"""


breadth=int(input("enter breadth of the triangle="))

height=int(input("enter height of triangle="))


area=(1/3)*breadth*height
print ("area of the triangle =",area)

"""

#5 Python Program to Swap Two Variables

"""
x=int(input("enter x value ="))
y=int(input("enter y value ="))

x,y=y,x
print("x =",x)
print("y =",y)

"""

#6 Python Program to Generate a Random Number
"""

import random
print(random.randint(0, 500))

"""

#7 Python Program to Convert Kilometers to Miles

"""

km=int(input("enter kilometers you want to convert ="))

miles = km*0.621371

print ("miles =",miles)

"""


#8 Python Program to Convert Kilometers to Miles


"""
celsius = int (input("enter celsius you want to convert ="))

faranheet =celsius*1.8+32

print ("faranheet =",faranheet)

"""

#9 Python Program to Check if a Number is Positive, Negative or 0

"""

num=int(input("enter any digit ="))

if num>0:
    print ("It is +ve integer ")
elif num<0:
    print ("It is -ve integer ")
elif num==0:
    print ("It\'s value is zero ")

"""

#10 Python Program to Check if a Number is Odd or Even

"""

num=int(input("enter any digit ="))
if num==0:
     print ("It\'s whole number")
elif num%2==0:
    print ("It\'s even number ")
elif num!=0:
    print ("It\'s odd number ")

"""

#11 Python Program to Check Leap Year

"""
year=int (input("enter a year "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("it is a leap year")
        else :
            print("it is not a leap year ")
    else:
        print("It is a leap year")
else:
    print("it is not a leap year ")


"""

#12  Python Program to Find the Largest Among Three Numbers
a=int(input("enter a ="))
b=int(input("enter b ="))
c=int(input("enter c ="))
if a>b:
    print (a)
elif b>c:
    print (b)
elif c>a:
    print (c)

else:
    print ("a=b=c")













