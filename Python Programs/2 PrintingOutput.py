x=2
y=5.1432

print ()
#Multiple lines
print (" some garbage ")
print (3)
print (x)
print (x+5)

print ()
#Same line
print ("some garbage " ,end="")
print (3 ,end=" ")
print (x ,end=" ")
print (x+5,end="")

print ()
#x and y are replaced by %d and % f
#The number of values in the brackets must match the number of % format operators within the string.
#Furthermore the type of format operator (%d, %f, %s) must match the data type of the value
print ("The answers are %d and %f"%(x,y))

print ()
#Formatting Numbers
#%4.1f means print the number in a column width of 4 and with one decimal place
#While %6.1f means a column width of 6 and one decimal place
#Numbers are always right-adjusted in their columns.
#Integers can also be formatted, e.g. to print an integer in a column width of 5 use %5d
print (" x  |  x**3")
print ("%4.1d|%6.1d"%(x ,x **3))
print ("%4.1f|%6.1f"%(y ,y **3))

print ()
#Table printing
x1 = 1.0
x2 = 10.0
clm1="x"
clm2="X**3"
print ("%4s|%6s"%(clm1 ,clm2))
print("-"*12)
print ("%4.1f|%6.1f"%(x1 ,x1 **3))
print ("%4.1f|%6.1f"%(x2 ,x2 **3))
