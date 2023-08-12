#using disjoint set

set1={'ranjani','amutha','pandian'}
set2={'anu','suresh','karthi'}
print(set1.isdisjoint(set2))
print("\n")

#print true if both sets have nothing as common
set1={'ranjani','amutha','pandian'}
set2={'anu','suresh','ranjani'}
print(set1.isdisjoint(set2))
print("\n")

#using subset
set1={'ranjani','amutha','pandian'}
set2={'anu','suresh','ranjani','amutha','pandian'}
print(set1.issubset(set2))
print("\n")


#using operator
print(set1<=set2)
print("\n")

#using superset
set1={'ranjani','amutha','pandian','anu','suresh',}
set2={'anu','suresh','ranjani'}
print(set1.issuperset(set2))
print("\n")


#using operator
print(set1>=set2)
print("\n")


#clear function will delete only set items but the set will be present
set2.clear()
print(set2)

#delete method will delete the whole set itself so the set is deleted from the memory itself
del set2
print(set2)


