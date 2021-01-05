
n=int(input("enter the size"))
l=list(map(int,input().split()))
l.sort()
res=l[-1]*l[-2]*l[-3]*l[-4]
print(float(res))



