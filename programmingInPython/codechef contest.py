from itertools import combinations
def digit(n):
    s=1
    for i in n:
        s*=int(i)
    return(s)
t=int(input())
c=0
pro=0
if t>=1 and t<=1000:
    
    for i in range(t):
        x=int(input())
        n=int(input())
        if (x<=1000 and x>=1 and n>=1 and n<=1000):
            
            l=list(map(int,input().split()))[:n]
            if all(i>=1 and i<= 1000 for i in l):
            
                s=""
                for i in l:
                    if i<x:
                        s+=str(i)
                    
                        
                l3= [''.join(j) for i in range(len(s)) for j in combinations(s, i+1)]
                for i in l3:
                    if len(i)==1:
                        c+=1
                    else:
                        pro=digit(i)
                        if pro<x:
                            c+=1
                        
                print(c)
