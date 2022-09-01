# using for loop please print all the prime numbers b/w 1-200 ,using For loop and Range Function

n1=1
n2=200

print("Prime numbers between", n1, "and", n2, "are:")

for num in range(n1, n2 + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
