

#using single value in a tuple
tuple1=(10)
print(type(tuple1))

tuple1=(10,)
print(type(tuple1))


#printing an tuple
tuple1=(12,0,-8,"ranjani",True,9,"hi",False,"queen",12)
tuple2=("welcome",19122003,"inside")
print(tuple1)
print(tuple2)

#print a particular index
print(tuple1[3])


#silicing
print(tuple1[:-2])
print(tuple1[-2:])
print(tuple1[::2])



554
#length of the tuple
print(len(tuple1))



#nestedtuple
tuple3=(tuple1,tuple2)
print(tuple3)
print(tuple3[1])
print(len(tuple3))


#using count
print(tuple1.count(12))



#using index it will only print the first occuring value's index
print(tuple1.index(12))


#concatenation tuple
tuple3=tuple1+tuple2
print(tuple3)
print(tuple3[1])
print(len(tuple3))




#they are unmutable and no deletion or addition occurs because they are ordered and we cannot change the order
tuple1[0]=34
print(tuple1)



