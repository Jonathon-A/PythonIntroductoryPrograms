#Functions
#Function naming convention is lower_case_with_underscores

#Function with no arguments
def print_line():
   print("==============================")

#Calling a function without arguments
print("before line")
print_line()
print("after line")

#Function with an argument
def print_line_of_length(length):
    for j in range(0,length):
        print ("=", end="")
    print()

#Calling a function with an argument
print("before line of length")
print_line_of_length(20)
print("after line of length")

#Function with multiple arguments and documentation string
def print_square(indent,side,symbol):
    """Prints indented square of characters:

      indent = leading spaces (int)
      side   = side length (int)
      symbol = character (str). """
    for j in range(0,side):
        print (indent*" " + side*(symbol + " " ))

#Calling a function with multiple arguments
print_square(5,5,'*')

#Printing documentation string of function using __doc__
print(print_square.__doc__)
print(print_line_of_length.__doc__) #returns none since documentation string not defined

#Conventions of documentation strings
"""
The first line should always be a brief summary of the function’s purpose (but not its name!). 
This line should begin with a capital letter and end with a full stop.
If there are more lines in the documentation string, the second line should be blank, visually separating the summary from the rest of the description. 
The following lines should be one or more paragraphs describing the function’s calling conventions, its side effects, etc."""

#Function that returns values
import math
def hypotenuse(x,y):
   # Returns the hypotenuse of a
   # triangle with sides x,y 
    hyp = math.sqrt(x**2+y**2)
    return hyp

def in_range(x):
   # Returns True if 0<x<1,
   #    False otherwise 
    if 0<x<1:
        return True
    else:
        return False

#Calling a function that returns a value - can also be called without using the returned value
print (hypotenuse(3,4))
print (in_range(3))
print (in_range(0.5))

