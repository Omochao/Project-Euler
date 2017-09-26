#Problem 2
#By considering the terms in the Fibonacci sequence whose values do not exceed four million,
#find the sum of the even-valued terms.
memo = [0,1]
def fib(n):
     if n < 2:
          return n
     elif n <= len(memo)-1:
          return memo[n]
     else:
          val = fib(n-1)+fib(n-2)
          memo.append(val)
          return val

n = 0
index = 0
while n < 4000000:
     n = fib(index)
     index+=1
print(sum([fib(n) for n in range(0,index-1,2)]))
