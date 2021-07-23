from array import *

#Example
tempartures = [
  [11, 12, 5, 2],
  [15, 6, 10],
  [10, 8, 12, 5],
  [12, 15, 8, 6]
]

#Accessing values

print(tempartures[0])
print(tempartures[1][2])

#Iteration
for r in tempartures:
  for c in r:
    print(c, end=' ')
  print()

#Inserting Values
tempartures.insert(2, [0, 5, 14, 11, 18])
print(tempartures)

#Deleting the values
del tempartures[1]
print(tempartures)