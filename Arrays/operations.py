"""
Basic operations on arrays.
1. Tranverse - Print all elements one by one.
2. Inserion - Adds an element at given index
3. Deletion - Deletes an element at given index
4. Search - Searches for an element, using the given index or by value
5. Updation - Updates an element at given index
"""

#Array is created in python by importing array module

#syntax
# from array import *
# arrayName = array(typecode, [initializers])
#Here typecode are the codes that are used to define the type of value the array will hold.
#For example, 'i' is for signed integer, 'I' is for unsigned integer, 'f' is for floating point.


# Example
from array import *

array1 = array('i', [10, 20, 30, 40, 50])

#Print all elements in array
for x in array1:
    print(x)

#Accessing Array Elements
#We can access elements by using indexing operator []
#Example
x = array1[0]
print(x)
y = array1[1]
print(y)

#Insertion
#We can insert an element at a given index by using the insert method
array1.insert(2, 60)
print(array1)

#Insert at End
array1.insert(len(array1), 60)
print(array1)

#Deletion
#We can delete an element by using the del keyword
#or
#Using remove() method
array1.remove(60) #Removes the first occurence of the element
print(array1)


#Search
#We can search for an element by using the index() method
indexOf40 = array1.index(40)
print(indexOf40)

#Updation
#We can update an element by reassigning a new value at desired index
array1[0] = 100
print(array1)