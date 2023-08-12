#find the sum of all the even numbers from 1 to 100 including 1 to 100


#method 1:
total=0
for i in range(1,101):
    if(i%2==0):
        total+=i
print(total)


#method 2:
total=0
for i in range(2,101,2):
    total+=i
print(total)
