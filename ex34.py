#operations in sets only symmetric  difference

#union-(set1 U set2)

#intersection-(set1 n set2)

#symmetric differnce-(set1 U set2)-(set1 n set2)


set1={'ranjani','amutha','pandian','kowsi'}
set2={'anu','suresh','ranjani'}
set3={'madhu','kowsi'}


#common values in both the sets are eliminated
print(set1.symmetric_difference(set2))


#symmetric differnce is not allowed for multiple sets
#print(set1.symmetric_difference(set2,set3))

#using operator
#print(set1 ^set2)

#symmetric differnce is allowed for multiple sets
#print(set1 ^set2 ^set3)

#update either values on the set1 or set2 but not on  the values of both the sets
set2.symmetric_difference_update(set1)
print(set2)


