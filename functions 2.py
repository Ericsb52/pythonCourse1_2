#Eric Broadbent
#9/18
import math
#get a users name
def get_name(name_input):
    
    name = name_input
    name = name.lower()
    name = name.title()
# step two display the name back for user
    print("the name you entered was", name)
# step 3 verify the name
    

print("this is our function")
name=input("whats your name")
get_name(name)


# calculate the area of a cricle
# radius*radius*pi
def areaOfCricle(radius1):
    pi=3.141592653
#1get a radius
    radius = radius1 
#2 calculat the area
    radius = float(radius)
    area=radius*radius*pi
#3 display the area
    print("the area of the cricle is: ",area)


#radiusx=input("what is the radius") 
#areaOfCricle(radiusx)

def pythagoras_theorem(ap,bp):
    #a^2+b^2=c^2
    a=float(ap)
    b=float(bp)
    c=a*a+b*b
    c=math.sqrt(c)
    print("the third side is ",c)




#pythagoras_theorem(3,4)


def add_numbers(x,y):
    num1 = x
    num2 = y
    num3 =int(num1)+int(num2)
    print(num1,"this is num 1")
    print(num2,"this is num 2")
    return num3

x=input("enter a number")
y=input("enter a second number")
num4=add_numbers()
num5=add_numbers()
print("the sum of your numbers is",num4)


























    
