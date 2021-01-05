l=[2, 3, 10, 6, 4, 8, 1]
m=l[0]-l[1]
for i in range(len(l)):
    for j in range(len(l)):
        if l[j]-l[i]>m:
            m=l[j]-l[i]
            
print(m)
