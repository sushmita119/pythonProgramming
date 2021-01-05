def fact(n):
    f=1
    print(n)
    if int(n) >=1:
        for i in range(1,int(n)+1):
            f = f*i
        print(f)
        return(f)
        
n=145
res=0
for i in str(n):
    
    res+=fact(i)
    
print("res t",res)
if res==n:
    print("strong")
else:
    print("not striong")
    
