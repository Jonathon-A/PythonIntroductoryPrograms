#While loop
"""
while condition:
    statements

if True then run the statements and loop again
if False then end loop
"""

#Loop that sums entered numbers
n = int (input("How many numbers? "))
count = 0
sum = 0
while count < n:
    num = int(input("Enter number " + str(count + 1) + ":"))
    count += 1
    sum += n
print("Total of entered numbers:", sum)

#Infitie loop with break statement
sum = 0
while True:
    n = int(input("Please enter a positive number"))
    if n >= 0:
        break
    print("The was a negative number, please try again")
    
print("Thanks for entering the positive number:",n)

#For loops
"""
for count in range(start, stop , step)
    statements

Loops until count increments above stop (starts at start and increments by step)
"""

print("For loop examples")
#Simple count (0 - 9)
for i in range (10):
    print(i, end="")
print()
#count from 1 to 10
for i in range (1, 11):
    print(i, end="")
print()
#count from 0 to 9 with increments of 3
for i in range (0, 10, 3):
    print(i, end="")
print()
#For loop table
Col1 = "i"
Col2 = "x"
Col3 = "x**2"
print("Creating table:")
k = int(input("Enter row count"))
x = float(input("Enter x value"))

print("%2s | %5s | %5s"%(Col1,Col2,Col3))
for i in range(k):
    print("%2d | %5.2f | %5.2f"%(i,x * i ,(x * i) **2))

