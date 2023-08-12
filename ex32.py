#operations in sets only intersection

#union-(set1 U set2)

#intersection-(set1 n set2)

#symmetric differnce-(set1 U set2)-(set1 n set2)


set1={'ranjani','amutha','pandian'}
set2={'anu','suresh','ranjani'}
set3={'madhu','kowsi'}

#intersection method 1
print(set1.intersection(set2))


#intersection method 2
print(set1 & set2)

#intersection method 3 nothing is common then it prints an empty set
print(set1.intersection(['deepa','oom']))

#intersetion method 4 update the values with set2 in set1 and print the common values
set1.intersection_update(set2)
print(set1)

#intersection method 5
print(set1.intersection_update(['deepa','oom']))
print(set1)
