#By considering the terms in the Fibonacci sequence whose values do not exceed four million,
#find the sum of the even-valued terms.
import time
memo = [1,2]
def fib(n):
     if n < 2:
          return memo[n]
     elif n <= len(memo)-1:
          return memo[n]
     else:
          val = fib(n-1)+fib(n-2)
          memo.append(val)
          return val
now = time.time()
print(sum([fib(i) for i in range(4000000) if fib(i) % 2 == 0]))
print(time.time() - now)
