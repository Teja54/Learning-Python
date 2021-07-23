from numpy import *

t = array(
  [
    ['Mon',18,20,22,17],
    ['Tue',11,18,21,18],
    ['Wed',15,21,20,19],
    ['Thu',11,20,22,21],
    ['Fri',18,17,23,22],
    ['Sat',12,22,20,18],
    ['Sun',13,15,19,16]
  ]) 

#Accessiong values

#Print data for wednesday
print(t[2])

#Print data for friday evening
print(t[4][3])


#Adding row
add_row_to_t = append(t, [['Avg',12,15,13,11]], 0) #Here 0 indicates row
print(add_row_to_t)

#Adding Column
