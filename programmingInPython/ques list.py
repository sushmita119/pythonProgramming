n=int(input())
l=list(map(int,input().split()))[:n]
l.sort()
s=0
for i in l:
    i+=2
    if((i+1)+(i-1))<i+2:
       k.append(i)
       i-=1
    else:
        s+=i
        i+=2
print(s)
        
   
