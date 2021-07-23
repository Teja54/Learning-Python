Days= set(["Mon","Tue","Wed","Thu","Fri","Sat"])

#Access  elements 
#We cannot access elements individually

#Be can make iteration:
for d in Days:
  print(d)


#Adding elements to the set
Days.add('Sun')
print(Days)


#Removing Item from a set
Days.discard('Sun')
print(Days)

#Union of Sets
#Union of two sets produces a set containing all the distinct elements from both the sets.
DaysA = set(['Mon', 'Tues', 'Wed'])
DaysB = set(['Wed', 'Fri', 'Sat', 'Sun', 'Thurs'])
AllDays = DaysA|DaysB
print(AllDays)


#Intersection of Sets
#Produces a new set containing only the common elements from both the sets.
CommonDays = DaysA & DaysB
print(CommonDays)

#Difference of Sets
#Produce a new set containing only the elements from the first set and none from the second set
Diff = DaysB - DaysA
print(Diff) #Here wed is not come in result


#Compare Sets
#We can check, if a given set set is a subset or superset of another set. The result will be true or false
set1 = set([1, 2, 3])
set2 = {1, 3, 2, 4, 5, 7, 9}
subset = set1 <= set2
superset = set2 >= set1
print(subset)
print(superset)
