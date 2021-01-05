
       
a=['q','w','e','r','t','y','u','i','o','p']
a1=['a','s','d','f','g','h','j','k','l']
a2=['z','x','c','v','b','n','m']
b=list(map(str,input().split()))
res=[]
for i in b:
    
    if (set(i) | set(a)) == set(a):
        res.append(i)
    elif (set(i) | set(a1)) == set(a1):
        res.append(i)
    elif (set(i) | set(a2)) == set(a2):
        res.append(i)
print(res)
        
