#What is the 10 001st prime number?
def sieve(n):
     return all((n-i)% (2*i+1)>0 for i in range(1,(n+1)//2))
def sundaram(it):
     return (2*n+1 for n in it if sieve(n))
primes = list(sundaram(range(100000)))
print(len(primes))
print(primes[10000])
