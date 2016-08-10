############################################################
#FILE: ex2a.py
#WRITER: orlykoren, orlykor12, 203595541
#EXERCISE: intro2cs ex2 2014-2015
#DESCRIPTION:
#a program that calculates perimeters and area
#output (screen)
#############################################################
import math #imported math moudle for farther using

# i call for myself to know which numbers represnt what
triangle= 3
rectangle= 1
circle= 2

#the user prints a number to choose a shape
input_shape= int(input("Choose a shape:"))

# a condition for choosing the num 1
if (input_shape == 1):
    input_width = float(input("width:")) # ask a num for width
    input_height = float(input("height:")) #ask a num for height
#then it calculates the area and the perimeter
    area = (input_width* input_height)
    perimeter = ((2*input_width) + (2*input_height))
    print("area:", area)
    print("perimeter:", perimeter)

#if its not the num 1 and its 2 then do that:
elif (input_shape == 2):
#put a num for radius
    radius = float(input("radius:"))
#then it calculates the area and the perimeter
    area = ((radius**2)*math.pi)
    perimeter = (2*math.pi*radius)
#print the results
    print("area:", area)
    print("perimeter:", perimeter)

#if its not the other two numbers and its 3, do that:
elif (input_shape == 3):
#put a numbers:
    a = float(input("a:"))
    b = float(input("b:"))
    c = float(input("c:"))
# it calculates the area and the perimeter
    perimeter = a+b+c
    new_p = (perimeter)/2
    area = math.sqrt(new_p*(new_p-a)*(new_p-b)*(new_p-c))
#print the results
    print("area:", area)
    print("perimeter:", perimeter)

#if not 1,2,3 then print:
else:
    print("Please enter a valid number for shape: 1 for rectangle, "    
          "2 for circle, or 3 for triangle")

#done

    
