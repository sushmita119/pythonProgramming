n=int(input())
l=[]
cost=0
for i in range(n):
    l.append(int(input()))
cost=l[0]+abs(l[1]-l[0])
for i in range(2,len(l)):
    t=min(l[:i])
    if t<l[i]:
        d=l[i]-t
        cost+=d
print(cost)
    
