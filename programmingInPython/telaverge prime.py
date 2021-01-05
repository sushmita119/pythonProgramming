from itertools import permutations as p
d={}
def perm(n):
    permu=[]
    l = list(p(str(n))) 
    for j in l:
        permu.append("".join(j))
    return(permu)
def prime(l,h):
    l1=[]
    for i in range(l,h):
        if i>1:
            for j in range(2,i):
                if(i % j==0):
                    break
            else:
                l1.append(i)
    
    for i in l1:
        res=perm(i)
        d[i]=res
                    
    print(d)
'''
    for i in l2:
        if int(i) in l1:
            l3.append(int(i))
    for i in l1:
        if len(str(i))==1:
            l3.append(int(i))
    print(l3)
    print(sorted(set(l3)))
'''

            

l,h=2,99
prime(l,h)

            
