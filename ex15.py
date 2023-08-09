#nested if-else for roller coster ride


height=int(input("Enter the height in feet:"))
age=int(input("Enter your age:"))
if height>=3:
    print("You can take the ride")
    if age<12:
        print("Pay 110 rs")
    elif age<=18:
        print("Pay 200 rs")
    else:
        print("Pay 250 rs")
else:
    print("You cannot take the ride")
