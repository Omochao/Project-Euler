#Find the sum of all the primes below two million.
limit = 2000000
def is_prime(n):
    if n == 2:
        return True
    elif n < 2:
        return False
    return not(any (n % x == 0 for x in range(2, int(n**0.5) + 1)))
print(sum([i for i in range(limit) if is_prime(i)]))
