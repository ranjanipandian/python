set1={10,34,54,True,1,10,"ran"}

#here an empty set is created but it is considered as empty dictionary only
set2={}
print(type(set1))
print(type(set2))

#an empty set is created
set2=set()
print(type(set2))

#changing the a particular value in a set is not possible
set1[2]=35
print(set1)

#add method is used to insert an element
set1.add(35)
print(set1)

#length method
print(len(set1))

#remove method is used to delete an element
set1.remove(35)
print(set1)

#if remove is used for the element that is not present in the set there comes an error
set1.remove(88)
print(set1)


#discard is used so no error occurs
set1.discard(88)
print(set1)

#clear method
set1 .clear()
print(set1)

#pop method
set1.pop()
print(set1.pop())
print(set1)

#entrie tuple can be added
set1.add((1,2,3,4))
print(set1)


#entrie list cannot be added because it is mutable
set1.add([1,2,3,4])
print(set1)

#only immutable data can be added because in set datas are stored in hash table


