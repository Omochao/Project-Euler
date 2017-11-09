f = open(r'C:\\Users\\Zyckr\\Documents\\Euler-Project\\txtfiles\\large_sum.txt', 'r', encoding='utf-8')
n = list(f)
nn = []
#print (f.readlines())
for i in n:
    s = ""
    for j in i:
        if j in "1234567890":
            s+=j
    nn.append(int(s))
print(str(sum(nn))[:10])
