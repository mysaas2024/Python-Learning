Name=['sli', 'ahmend','hello']
print(Name)

#add an (one item) items in the Listwe use append

Name.append('hamza')
print(Name)

#add more than one value 

Name.extend(["dfd",2])

print(Name)

#add a thing at a index
Name.insert(3,453)
print(Name)

#removing the items
# removing by name  
Name.remove('sli')
print(Name)

#removing by last
Name.pop()
print(Name)

#removing by index 
Name.pop(3)
print(Name)

#Sorting of List 
Ages=[232,434,323,4232,2323,23,2,24]
print(Ages)
Ages.sort(reverse=True)
print(Ages)
Ages.sort(reverse=False)
print(Ages)
#sort by some point value
Ages.sort(key=3)
print(Ages)

