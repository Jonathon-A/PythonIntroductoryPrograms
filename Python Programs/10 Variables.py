#Variables

#Global variable
#Definied inside and outside of function
gsymbol = '*'

def print_square(indent,side):
    #Local variable
    #Only defined within function
    lsymbol= "^" 
    for j in range(0,side):
        print (indent*" " + side*(gsymbol+lsymbol))
print_square (0,3) 

sums = 0

def add_to_sum(n):
    global sums
    sums += n
   


add_to_sum(9)
print(sums)
