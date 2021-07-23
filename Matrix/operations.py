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
add_column_to_t = insert(t, [5], [[1], [2], [3], [4], [5], [6], [7]], 1) #Here 1 indicates column
print(add_column_to_t)

#Deleting a row
t = delete(t, [2], 0) #0 for row 1 for column
print(t) #Deleted wednesday row

#Deleting a column
t = delete(t, [2], 1) #1 for column
print(t) #Deleted 3 column

#Updating row 
t[2] = ['Wed', '15', '20', '19'] #Resigning row
print(t)

