l=[1,2,2,3,3,3,4,4,5,5,5,5,6,6,6,7,8,9,10]
#s=set(l)
#print(s)
d={}
for i in l:
    c=l.count(i)
    d[i]=c
#print(d)
for i in sorted(d.values()):
    print(d.items())
    
