#Problem 3
#What is the largest prime factor of the number 600851475143?
from math import sqrt
from math import trunc
def is_prime(n):
     if n == 1:
          return False
     elif len(factors(n)) > 2:
          return False
     else:
          return True
def factors(n):
     d = [i for i in range(1,trunc(sqrt(n))) if n%i==0]
     d.append(n)
     return d
def prime_factors(n):
     d = factors(n)
     e = []
     for i in d:
          if is_prime(i) == True:
               e.append(i)
     return e
print(prime_factors(600851475143))
