#Dictionary data structure
#Dictionaries contain pairs of data: the key and its associated value(key instead of index)
#There can be no duplicate kets

#dictionary
d = {'one':'un', 'two':'deux'} 
#'two':'deux' is a key:value pair,
#'two' being the key and 'deux' being the value

#empty dictionary
d = {}

#dictionary examples
d = {'age':33, 'height':1.6}
d = {'a':[1,2,3], 'b':[7,8,9]} 
d = {'one':'un', 'two':'deux'}
print (d)

#Indexing a Dictionary
print (d['two']) #returns 'deux'
print ("Value with key 'two':",d)

#Adding to a dictionary
d['four'] = 'quatre'
print ("added 'quatre' with key 'four':",d)

#Deleting from a dictionary
del (d['two'])
print ("deleted value with key 'two':",d)

#Testing Membership
#Returns true if key is in dictionary
print ("Is a value with key 'two' in dictionary:",'two' in d)  #return True
print ("Is a value with key 'two' in dictionary:",'deux' in d) #return False


#Creating Dictionaries from Lists

#The dict function will convert a list of two-element lists into a dictionary
pairs=[['one','un'],['two','deux']]
d = dict(pairs)
print ("dictionary created from list of pairs:",d)

#If keys and values are in separate lists then one can use the following method
keys = ['one', 'two']
values=['un',  'deux']
pairs = zip(keys,values)
print ("list of pairs created from two lists:",pairs)
d = dict(pairs)
print ("dictionary created from two lists:",d)


#Dictionary Methods
#All of the following are non-mutating, i.e.  they don't alter the dictionary itself
print("Dictionary Methods:")

#Returns a copy of the dictionary
print(d.copy()) 

#Returns “a list” of all the key,value pairs in d
print("dictionary items:")
print(d.items())
print(list(d.items())) 

#Returns “a list” of all the keys in d
print("dictionary keys:")
print(d.keys()) 
print(list(d.keys())) 

#Returns “a list” of all the values in d
print("dictionary values:")
print(d.values()) 
print(list(d.values())) 

#Returns d[k] if k is a key in d, x otherwise. Useful when you are not sure whether a key exists
print(d.get('one','not here'))
print(d.get('yikes','not here')) 


#Looping through a Dictionary
d={'A': 80, 'C': 55, 'B': 65, 'D': 45}
print("Dictionary Loop")
for key in d.keys():
    print (key, d[key])
    
print("Sorted Dictionary Loop")
sortedkeys =sorted(d.keys())
for key in sortedkeys:
    	print (key, d[key])

#Find a particular key
val = 55
for key in d.keys():
    if d[key]==val:
    	print( key)


