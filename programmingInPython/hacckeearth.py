def digit(n):
    s=0
    for j in str(n):
        if int(j)>0 and (s-int(j)!=7):
            s+=int(j)
        else:
            return False
    return s
def digit2(n):
    s=0
    for j in str(n):
        if int(j)>=0:
            s+=int(j)
        else:
            return False
    return s
        
b,k=[int(j) for j in input().split()]

c=0
for i in range(1000):
    if len(str(i))==k:
        add=digit(i)
        if add!=False and len(str(add))==2:
            add2=digit(add)
            if add2!=False and len(str(add2))==1:
                if add2 == b:
                    print(i)
                    c=1
                    break
if c<0:
    print("-1")
    
    
                
   
                
            
        
    
