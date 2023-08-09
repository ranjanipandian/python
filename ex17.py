#using multiple statements of if

age=int(input("enter the age:"))
if age<12:
    bill=150
    print("your ticket price is 150")
if age<18:
    bill=200
    print("your ticket price is 200")
else:
    bill=400
    print("your ticket price is 400")


    
photo=(input("do you need photo or not:"))
if photo=='Y' or 'y':
    bill+=50
    print(f"your total bill is:{bill}")
else:
    print("you are not a valid customer")
    
    
