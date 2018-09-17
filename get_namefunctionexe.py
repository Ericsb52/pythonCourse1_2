#Eric Broadbent
#9/18
#get name function
import math

def get_name(name):
    input_name = name
    input_name=input_name.lower()
    input_name=input_name.title()

    print("the name you entered was",input_name)
#verify name
    input ("is this correct yes or no ")

print("this is our function")
#ask user for name
name=input("what is your name")
#display name
get_name(name)

def areaOfCricle():
    PI = 3.14159265
#1 get a radius
    x = input("what is the radius")
#2 compute te area
    radius = float(x)
    area= radius*radius*PI
#3 display information
    print("the area of the cricle is: ",area)

#areaOfCricle()


def pythagoras_theorem(ap=1,bp=1):
    a=float(ap)
    b=float(bp)
    c=a*a+b*b
    c=math.sqrt(c)

    print ("the third side is",c)



    

#pythagoras_theorem(3,4)

def add_numbers(x,y):
    num1= x
    print("num1 = x " ,num1)
    num2= y
    print("num2 = y ",num2)
    num3= int(num1)+int(num2)
    return num3

x=1
y=-9
#num4 = add_numbers(x,y)
print(num4)














