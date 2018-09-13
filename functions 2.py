#Eric Broadbent
#9/18

#get a users name
def get_name():
    
# step one ask user for name
    name=input("whats your name")
# step two display the name back for user
    print("the name you entered was", name)
# step 3 verify the name
    input("is this correct yes or no ")

print("this is our function")
#get_name()


# calculate the area of a cricle
# radius*radius*pi
def areaOfCricle():
    pi=3.141592653
#1get a radius
    radius = input("what is the radius") 
#2 calculat the area
    radius = float(radius)
    area=radius*radius*pi
#3 display the area
    print("the area of the cricle is: ",area)

areaOfCricle()











    
