"""
Matrix is a special case of two dimensional array, where, each data element is of strictly same size.
Every matrix is also a two dimensional array but not vice versa
"""

#Import 
from numpy import *  
a = array([['Mon',18,20,22,17],['Tue',11,18,21,18], 
     ['Wed',15,21,20,19],['Thu',11,20,22,21], 
     ['Fri',18,17,23,22],['Sat',12,22,20,18], 
     ['Sun',13,15,19,16]]) 
     
m = reshape(a,(7,5)) 
print(m) 