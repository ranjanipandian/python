#WAP will select a random name from a list of names and the person selected will have to pay everybody's food bill with using choice method

import random
name=input("Enter everybody's name seperated by comma:")
s=name.split(",")
length=len(s)
choice=random.randint(0,length-1)
print(f"{s[choice]} will pay the bill")



#using choice method
import random
name=input("Enter everybody's name seperated by comma:")
s=name.split(",")
p=random.choice(s)
print(f"{p} will pay the bill")
