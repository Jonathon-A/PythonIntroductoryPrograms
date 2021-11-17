#String literals
print("\'Single quote")
print("\"Double quote")
print("\nNewline")
print("\tTab") 

#String operators
s = "1"
print("* operator:",s * 10)
print("+ operator: " + s)

#String indexing
string = "abcdef"
print("First letter:", string[0])
print("Third letter:", string[2])
print("Last letter: ", string[len(string)-1])
print("Last letter: ", string[-1])
print("Second to last letter:", string[-2])
print()

#String slicing
town="Loughborough"
#s[i:j] is the substring of s from the ith element, included, to the jth element, excluded
print (town[2:5]) #letter indexes 2 - 4
print (town[:5])  #letter indexes 0 - 4
print (town[5:])  #letter indexes 5 - end
print()

#String length (len)
print("String length:", len(town))
print()

#String methods
s = "Jonathon"
print(s.lower()) #Returns a copy of s with all letters converted to lowercase
print(s.upper()) #Returns a copy of s with all letters converted to uppercase
print(s.count("o")) #Returns the number of occurrences of substring in s
print(s.replace("o","a")) #Returns a copy of s with the first substring replaced by the second string
print(s.strip("on")) #Called without an argument, s.strip() returns a copy of s with both
print()              #leading and trailing whitespace removed. Called with a string argument,
                     #it removes any leading or trailing characters contained the string

#String split
print("Split string:")
s="oak trees, hazel shrubs"
print (s.split(" "))
print (s.split(","))
#String join
print("\nJoint string:")
l = ["oak","hazel","beech"]
s = "; ".join(l)
print (s)
