#import modules
import math
y = math.sin ( math.pi/6.0 )
print(y)

#Renaming modules
import math as ma
y = ma.sin ( ma.pi /6.0 )
print(y)

# new random number
import random
r = random.random ()
print (r)

print()
#list the functions within a module
print( dir (math))

"""
You need to install the python modules 
A package contains all the files you need for a module.
Use PIP command for the package installation
 PIP is a package manager for Python packages
Install PIP
You can download and install it from the link below: https://pypi.org/project/pip/
Find Packages
Find more packages at https://pypi.org/
Example modules  
pip install graphviz (http://www.graphviz.org/)
pip install matplotlib (https://matplotlib.org/)
"""
