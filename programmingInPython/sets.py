n=int(input())
l1=list(map(int,input().split()))[:n]
m=int(input())
l2=list(map(int,input().split()))[:m]
a=set(l1)
b=set(l2)
l3=list(a.difference(b))
l4=list(b.difference(a))
l5=list(l3+l4)
l6=sorted(l5)
for i in l6:
    print(i)
