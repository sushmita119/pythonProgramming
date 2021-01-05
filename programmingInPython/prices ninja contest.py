t=int(input())
c=0
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))[:n]
    for i in range(n+1):
        for j in range(i+1,n+1):
            if l[i]>l[j]*l[j]:
                c+=1
print(c)
