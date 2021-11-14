#Logical Expressions
"""
2<3 = True 
3<2 = False
3=2 = False 
"""

#Relational Operators
"""
>
<
<=
>=
==
!= 
"""

a=7
b=5
print (b<a, b>a, b==a, b!=a)

#if condition:
#    statement(s)

try:
    temp = int(input("Please enter a number"))
    IsInt = True

except:
    IsInt = False 

#If example 1
if(IsInt):
    print("That is an integer!")
else:
    print("That is not an integer!")

system = input("please select your operating system \n m (Mac), w(Windows), u(Unix):")

if system=="m": 
    print ('www.apple.com') 
elif system=="w":
     print ('www.microsoft.com')
else: 
    print ('www.unix.com')
print ('bye')

#If example 2
age = int(input ("How old are you? "))

if age <5:
	print (" That 's a bit young")
elif 5< age <18:
	print ("You should be in school")
elif 18 <= age <65:
	print ("You should be at work ")
elif age >65:
	print ("You are retired ")
print ("Bye")

#Logical operators
"""
and
or
not
"""

a=7
b=5
c=5
print (a>b and b==c)
print (not(a>b))
print (a<b or b==c)


