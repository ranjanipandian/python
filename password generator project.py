#password generator project

#Excpected output:

#Welcome to the Password Generator!

#How many letters would you like in your password?

#4

#How many symbols would you like?

#3

#How many numbers would you like?

#2

#9eSn)n*&9

import random

letters=['A','B','C','D','E','F','G','H','I','K',
         'L','M','N','O','P','Q','R','S','T','V','X','Y','Z',
         'a','b','c','d','e','f','g','h','i','j','k ','l','m','n',
         'o','p','q','r','s','t','u','v','w','x','y','z']

numbers=['0','1','2','3','4','5','6','7','8','9','0']

symbols=['!','@','#','$','%','^','&','*','(',')']

print("Welcome to the Password Generator!")

l=int(input("How many letters would you like in your password?\n"))

n=int(input("How many numbers would you like in your password?\n"))

s=int(input("How many symbols would you like in your password?\n"))

password_list=[]

for i in range(1,l+1):
    x=random.choice(letters)
    password_list += x

for i in range(1,n+1):
    x=random.choice(numbers)
    password_list += x

for i in range(1,s+1):
    x=random.choice(symbols)
    password_list += x
print("printing without shuffling:",password_list)

random.shuffle(password_list)
print("printing with shuffling:",password_list)
password=""
for i in password_list:
    password += i
print("strong password:",password)

    
