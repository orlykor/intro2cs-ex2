############################################################
#FILE: ex2b.py
#WRITER: orlykoren, orlykor12, 203595541
#EXERCISE: intro2cs ex2 2014-2015
#DESCRIPTION:
#a program that calculates numbers
#output (screen)
#############################################################
import math #imported math moudle for farther using

# ask to put a number and an operator
num1 = int(input("num1:"))
num2 = int(input("num2:"))
operation = input("operation:")

#conditions for variables operators
if(operation == '+'):
    adding = num1 + num2
    print(adding)

#if not + and its -, do:
elif(operation == '-'):
    reducing = num1 - num2
    print(reducing)

#if not +, not - and its * do:
elif(operation == '*'):
    multiply = num1 * num2
    print(multiply)

#if not all the others and its / do:
elif(operation == '/'):
    if (num2 == 0): # print that if its 0
        print("Can't divide by 0")
    else:      # if its not, continue
        divide = num1 // num2 #i want it without the remains
        print(divide)

elif(operation == '%'):
    if(num2 == 0): # print that if its 0
        print("Can't divide by 0")
    else:  # if its not, continue
        modulo = num1 % num2
        print(modulo)

# if it's nothing of the above- print that
else: 
    print("Unknown operator")
    #done
