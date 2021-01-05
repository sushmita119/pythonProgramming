n=int(input())
count=0
l=[]
l2=[]
for i in range(n):
    l.append(input())
for i in range(len(l)):
    if l.count(l[i])>count:
        count=l.count(l[i])
        index=i
    elif l.count(l[i])==count:
        l2.append(l[i])
        l2.append(l[index])
l2.sort()
print(l2)
print(l2[-1])
        
        
