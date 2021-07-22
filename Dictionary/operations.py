#Accessing values in Dictionary
dict = {
  'name': 'teja',
  'age': 20,
  'profession': 'software developer'
} 
print("dict['name']: ", dict['name']) 
print("dict['age']: ", dict['age'])

#Updating values in Dictionary
dict['age'] = 19 #update existing entry
dict['degree'] = 'BTECH' #Add new entry

print(dict)


#Deleting Dictionary Elements

del dict['name'] #remove entry with key 'name'
dict.clear() #empties the list
del dict #delete entire dictionary

