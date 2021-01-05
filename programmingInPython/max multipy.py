n=int(input())
l=list(map(int,input().split()))
l.sort()
if all(i>0 for i in l):
    print(l[-1]+l[-2])
else:
    p1,p2=l[0],l[1]
    n1,n2=l[-1],l[-2]
    if (p1*p2)>(n1*n2):
        print(p1+p2)
    else:
        print(n1+n2)
        
