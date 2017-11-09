f = list(open(r"C:\\Users\\Zyckr\\Documents\\Euler-Project\\txtfiles\\maximum_path_sum.txt", 'r', encoding='utf-8'))
tri = []
print(f)
for i in f:
    i = i.rstrip()
    k = i.split()
    for n in k:
        tri.append(int(n))
f = open("C:\\Users\\Zyckr\\Documents\\NetBeansProjects\\Problems\\newfile.txt", 'w')
for i in tri:
    f.write(str(i) + "\n")
f.close()
#for row in range(13):
 #   for col in range(len(tri[row])-1):
 #       tri[row][col] = max((tri[row][col] + tri[row][col+1]), (tri[row]+tri[row+1][col+1]))
        #print(tri[row][col])
