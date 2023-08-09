#check whether a leap year or not
year=int(input("Enter the year to be checked:"))
if year%4==0 and year%100!=0 or year%400==0:
    print("Yes it is an leap year")
else:
    print("No not an leap year")
