#list program with all its functions

values=[21,44,"ranjani","19.12.2003",17.1203,7777,"pandian","how are you",44,8,82.90,"coimabtore","1234567890"]

#print the whole list
print(values)

#print the particular element alone
print(values[2])
print(values[1])

#print the length of the whole list
print(len(values))

#print the length of the particular element list
print(len(values[2]))

#backward indexing
print(values[-2])


#silicing
#(last index-1) will be printed in silicing
print(values[0:6])
print(values[3:10])
#leave one index and will be printed
print(values[0:12:2])

print(values[0:12:4])

#sorting a list
#duplicates are allowed in list
numbers=[10,20,30,40,50,10]
numbers.sort()
print(numbers)

#reverse a list
numbers.reverse()
print(numbers)

#append a list
#the element will be added at the end
numbers.append(45)
print(numbers)

#insert  an element in list
numbers.insert(1,45)
print(numbers)

#extend an several elements at the end of the list
numbers.extend([1,2,3,4,5,6,7,8,9,0])
print(numbers)

#change the element
numbers[1]=15
print(numbers)

#change several elements using indexing
numbers[1:4]=[45,46,47]
print(numbers)

#remove an element
numbers.remove(0)
print(numbers)

#remove the duplicate element
numbers.remove(10)
print(numbers)

#pop an element means remove the last element
print(numbers.pop())
print(numbers)

#count
print(numbers.count(10))



