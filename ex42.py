#program to find maximum from a list of numbers

numbers=input("Enter the numbers:")
numbers_list=numbers.split()
print(numbers_list)
c=0
for i in numbers_list:
    c+=1
print(c)   
for i in range(c):
    numbers_list[i]=int(numbers_list[i])
max=numbers_list[0]
for i in numbers_list:
    if i>max:
        max=i
print("The maximum number is:",max)
