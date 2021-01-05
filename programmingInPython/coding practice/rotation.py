T=int(input())
l=[]
temp=[]
for i in range(0,T):
   n,k = map(int,input().split()) 
l=list(map(int,input().split()))[:n]
for i in range(k):
    temp.append(l[n-2])
    n+=1
le=len(l)-2
for i in range(0,(le)):
    temp.append(l[i])
print(*temp)
