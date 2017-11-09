#Problem 4
#Find the largest palindrome made from the product of two 3-digit numbers.
import math
def factors(n):
     return [i for i in range(1, math.trunc(n/2)) if n%i==0 and len(str(i)) == 3]
def is_palin(n):
     return str(n) == str(n)[::-1]
a = []
for i in range(900,1000):
     for j in range(900,1000):
          if is_palin(i*j):
               a.append(i*j)
print(max(a))
