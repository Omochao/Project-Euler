#Problem 5
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def smallest_positive_num(n):
     i = 1
     j = 2
     while j < n:
          if i%j !=0:
               i+=1
               j=2
     return i
print(smallest_positive_num(10))
