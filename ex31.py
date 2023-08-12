#operations in sets only union

#union-(set1 U set2)

#intersection-(set1 n set2)

#symmetric differnce-(set1 U set2)-(set1 n set2)


set1={"ranjani","anu","suresh"}
set2={"amutha","pandian","ranjani"}
set3={"Manoj","subi"}

#union method 1 the sets can be of different type
print(set1.union(set2))
print(set2.union(set1))

#union method 2 all the sets that are passed as argument should be of same type
print(set1 | set2)

#union method 3
print(set1.union(set2,set3))

#union method 4
print(set1.union(('priya','vanitha')))
print(set1 |('priya','vanitha'))

#union update with 3 methods
set1.update(set2)
print(set1)

#set1.update(['Amutha','diya'])
print(set1)


set1|=set2
print(set1)






















