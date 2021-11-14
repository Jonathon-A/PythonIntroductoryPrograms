#A list is an ordered set of values or elements,
#where each value is identified by an index
#The elements can be of any data type
print  (["Bread","Milk","Tea","Soap"]) #Strings
print  ([2,9,24,13])      # Integers
print  ([2,3.142,"xyz"])  # Mixed types
print  ([])               # Empty list

#Assignment
sci=["Physics","Chemistry","Biology"]
print (sci[0])
print (sci[2])

#Looping through list
shopping = ["Bread","Milk","Tea","Soap"]
for item in shopping:
    print(item)
i = 0
while i<4:
  print (shopping[i])
  i = i+1

#List length
print(len(shopping))

#List Operations
pets=["dog","cat","rat","fish"]
print(pets)

#Indexing a list
print(pets[2])  #returns 'rat'

#Changing a list element
pets[2]="gerbil"

#Deleting Elements
del (pets[2])

#Adding a List Element
pets=pets+["hampster"] 
pets.append("fish")     #Appends element to the end of the list
pets.insert(2,"rat")    #Inserts element at index specified in the list
print(pets)

#Adding two lists
a = [1,3,5]
b = [1,2,3]
c = [0,0,0]
for j in range(0,3):
    c[j]=a[j]+b[j]
print(c)

#Largest number
x = [30,16,70,30,30,30,60,109,40,67]
max = x[0]
index = 0
for i in range(len(x)):
    if x[i] > max:
        max = x[i]
        index = i
print(index,max)

#Sorting list
x.sort()
print(x)
