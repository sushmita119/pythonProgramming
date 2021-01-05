ns=int(input())
l=list(map(int,input().split()))[:ns]
stu=int(input())
l2=list(map(int,input().split()))[:stu]
l2.sort()
c=l2[-1]
c2=0
for i in l:
    if i<c:
        c2+=1
print(c2)
    
