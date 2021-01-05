from itertools import combinations
l2=[]
l3=[]
n=int(input())
l=list(map(int,input().split()))[:n]
lenght= int(input())
comb = combinations(l,lenght)

for i in list(comb):
    l2.append(i)
res =[int("".join(map(str,i))) for i in l2]
print(res)
for i in res:
    print(i)
    if i%3==0 and len(str(i))==lenght:
        l3.append(i)
print(l3)
print(min(l3))


