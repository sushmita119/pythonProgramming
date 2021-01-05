T=int(input())
l=[]
temp=[]
c=0

for i in range(0,T):
   n,k = map(int,input().split()) 
l=list(map(int,input().split()))[:n]
for i in range(n-1,0):
    temp.append(l[i])
print(temp)
    
