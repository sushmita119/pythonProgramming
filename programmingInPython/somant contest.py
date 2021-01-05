from itertools import combinations
t=int(input())
while(t!=0):
    t-=1
    n=int(input())
    l=list(map(int,input().split()))[:n]
    l.sort()
    s=2*l[0]
    no=0
    comb=combinations(l,2)
    for i in list(comb):
        j=list(i)
        if(j[0]>2*j[1] or j[1]>2*j[0]):
            no+=1
    print(no)

    
'''	
#for i in range(len(a)):
    l2=[]
for j in combinations(a, 2):
    l2.append("".join(j))
for i in l2:
    no+=1
print(no)
'''

