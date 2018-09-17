import math

def pythagoras_theorem():
    a=int(input("enter the first side of the triangle"))
    b=int(input("enter the second side of the triangle"))
    c=a*a+b*b
    c=math.sqrt(c)
    print("the third side is ",c)

pythagoras_theorem()
