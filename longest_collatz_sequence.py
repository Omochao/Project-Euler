def collatz(n):
    i = 0
    while n != 1:
        if n%2==0:
            n//=2
        else:
            n = 3*n+1
        i+=1
    return i
m = 9
for i in range(2, 1000000):
    if collatz(i) > collatz(m):
        m = i
print(m)
