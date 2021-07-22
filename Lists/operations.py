#Accessing values in a list
list1 = [1,2,3,4,5]
print("list1[0]: ", list1[0])

#Slicing a list
print("list1[1:5]: ", list1[1:5])

#Updating the list 
list1[0] = 10
print(list1)

#Deleting list element
del list1[0]
print(list1)

#Other Operations on list
#length
print(len(list1))

#Concatenation
list2 = [6,7,8]
list3 = list1 + list2
print(list3)

#Repetition
print(list1 * 3)

#Membership
print(3 in list1)

#Iteration
for x in list3:
  print(x)