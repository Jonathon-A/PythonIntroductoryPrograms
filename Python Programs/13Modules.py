#Once imported, you can use any function declared in the module
import math
#Shows available functions
help(math)


import sys
sys.path.append('MyModuleExample')

#Looks for module "Fibonacci" in same file location
#If not found then looks in folder "MyModuleExample"
import Fibonacci as f

f.print_series(1000)
print()

#prints name of funtion
print(f.__name__)

#You can rename imported functions
print_fibonacci_series = f.print_series
print_fibonacci_series(500)
print()

#imports all names that module defines
from Fibonacci import *
print_series(100)
print()

#Import specific module from folder "MyModuleExample"
import MyModuleExample.Fibonacci
MyModuleExample.Fibonacci.print_series(50)
print()

if __name__ == "__main__":
    print("testing")
    #testing print series
    print_series(20)
    #testing code written here
    fList = return_list(10)
    print("\nFibonacci numbers up to 10")
    print(fList)
