l=[16, 17, 4, 3, 5, 2]
l3=[]
for i in range(len(l)):
    l2=[]
    l2=l[i+1:]
    l2.sort()
    if len(l2)!=0:
        if l[i]>l2[-1]:
            l3.append(l[i])
l3.append(l[-1])
print(*l3)
