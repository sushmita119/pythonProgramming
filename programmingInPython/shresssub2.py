n=int(input())
s=list(map(int,input().split()))[:n]
c=list(map(int,input().split()))[:n]

res = []
for j in range(1,n+1):
    tot=0
    
    for i in range(n):
        
        
        tot+=abs(j-s[i]) * c[i]
        
    res.append(tot)
    
print(min(res))
        
        
