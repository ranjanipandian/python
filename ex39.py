#for else in python
#the statement of else will be executed only if the for loop is executed completely without terminating


tuple=(1,2,76,5,9)
for i in tuple:
    print(i)
    if i==5:
        break
else:
    print("loop is successfully completed without termination")
    

