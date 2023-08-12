#fizzBuzz job interview question


#explanation is:
#print the numbers from 1 to n and if the no is divisible by 5 then print buzz and divisible by 3 print buzz and divisible by 3 and 5 print fizzbuzz or else print the no


n=int(input())
for i in range(1,n+1):
     if i%3==0 and i%5==0:
        print("FizzBuzz")
     elif i%3==0:
         print("Fizz")
     elif i%5==0:
         print("Buzz")
     else:
         print(i)
print("The program is executed successfully")
