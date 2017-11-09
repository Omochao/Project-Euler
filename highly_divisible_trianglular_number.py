from math import ceil
def T(n):
    return (n*(n+1))//2
def divisors(n):
    return len([x for x in range(1, ceil(n**0.5)+1) if n%x==0])*2
i = 0
k = 0
while k < 500:
    k = divisors(T(i))
    i+=1
print(T(i-1))

