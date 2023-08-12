#exercise to calculate average height from a list of heights by using for loop and get input from the user and the output shoulsd be the nearset whole number


height=input("enter all the heights:")
height_list=height.split()
c=0
for i in height_list:
        c=c+1
print(c)
for i in range(c):
    height_list[i]=int(height_list[i])
print(height_list)


sum=0
for i in height_list:
    sum+=i
print("So the average is:",round(sum/c))





