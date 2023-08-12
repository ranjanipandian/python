#operations in sets only  difference

#union-(set1 U set2)

#intersection-(set1 n set2)

#symmetric differnce-(set1 U set2)-(set1 n set2)


set1={'ranjani','amutha','pandian','kowsi'}
set2={'anu','suresh','ranjani'}
set3={'madhu','kowsi'}

#differnece method 1 print the uncommon values in set that is passed at first
print(set1.difference(set2))

#differnece method 2
print(set1-set2)


#differnce method 3
print(set1.difference('priya','vaishali'))
print(set1.difference('priya','pandian','amutha'))

#differnce method 4
print(set1.difference(set2,set3))

#differnce method 5
set1.difference_update(set2)
print(set1)

