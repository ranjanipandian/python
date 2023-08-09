#love calculator

a=input("Enter the name one: ")
b=input("Enter the name two: ")

combined_string=a+b

lowercase_string=combined_string.lower()

t=lowercase_string.count('t')
r=lowercase_string.count('r')
u=lowercase_string.count('u')
e=lowercase_string.count('e')

true = t + r + u + e

l=lowercase_string.count('l')
o=lowercase_string.count('o')
v=lowercase_string.count('v')
e=lowercase_string.count('e')

love = l + o + v + e


love_score = int(str(true) + str(love))

if love_score < 10 or love_score>90:
    print(f"Your score is {love_score} and you go together like coke and mentos")
elif love_score>=40 or love_score<50:
    print(f"Your score is {love_score} and you are alright together")
else:
    print(f"Your love_score is {love_score}")
     
