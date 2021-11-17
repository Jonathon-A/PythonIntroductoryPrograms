#Opening a file (open())
#The first argument is a string containing the filename
#Second argument:
#'r' when the file will only be read
#'w' for only writing (an existing file with the same name will be erased)
#'a' opens the file for appending; any data written to the file is automatically added to the end. 
#'r+' means opening file for both read and write 

#Reading line from a file
f = open("12poem.txt","r")
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
f.close()
print (line1 + line2 + line3)

#Reading all lines in a file
#While loop method
f = open("12poem.txt","r")
while True:
    line = f.readline()
    if line == "": #Stops at empty line
        break
    print(line.strip("\n"))
f.close()
print()
#For loop method
f = open("12poem.txt","r")
for line in f:
    print(line.strip("\n"))
f.close()


#Writing over a file (deletes previous lines)
f = open("12poem.txt","w")
newlines = "Baa, baa, black sheep\n\
Have you any wool?\n\
Yes sir, yes sir, three bags full.\n\
One for the master,\n\
And one for the dame,\n\
And one for the little boy\n\
Who lives down the lane."
f.write(newlines)
f.close()


#Writing new lines to file
f = open("12poem.txt","a")
newline = "New line added"
f.write("\n")
f.write(newline)
f.close()
