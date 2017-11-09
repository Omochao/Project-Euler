memo = {}
def routes(n,k):
    if n == 0 or k ==0:
        return 1;
    elif (n,k) in memo:
        return memo[(n,k)]
    else:
        new=routes(n,k-1)+routes(n-1,k)
        memo.update({(n,k):new})
        return memo[(n,k)]
print(routes(20,20))
