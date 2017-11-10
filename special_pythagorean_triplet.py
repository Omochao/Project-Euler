#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
s = 1000
for i in range(2,s//3):
     for j in range(i,s//2):
          k = s - i - j
          if i**2 + j**2 == k**2:
               print(i)
               print(j)
               print(k)
