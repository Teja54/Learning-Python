#Accessing tuples

tup1 = ('physics', 'chemistry', 1997, 2000) 
tup2 = (1, 2, 3, 4, 5, 6, 7 ) 
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

#Updating Tuples
#Since tuple are immutable(unchangeable) we cannot update or change values
tup3 = (12, 34, 56)
tup4 = ('abc', 'xyz')

#tup3[0] = 100 
#print(tup3) #Gives Error

#But we can add two or tuples
tup5 = tup3 + tup4
print(tup5)

#Another way of Update Tuple is
tup = ('a', 'b', 'c', 'd')
#step1: Convert to list
y = list(tup)
#step2: Add elements to list
y.append('e')
#Step3: convert back to tuple
tup = tuple(y)
print(tup)

#Deleting Tuple
#Since tuple are immutable(unchangeable) we cannot delete or remove individual values
#But it is possible to delete whwole tuple completely
del tup #Deleted tuple completely
#print(tup)

#Another method of delete or remove individual values
#Example
tup6 = ('1', '2', 'a', '3')
#Step1: convert to list
z = list(tup6)
#Step2: Remove individual element from list
z.remove('a')
#Covert back to tuple
tup6 = tuple(z)