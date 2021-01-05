n=int(input())
n=list(str(n))

c=0

for i in range(len(n)-1):
 
    if int(n[i])+int(n[i+1]) == 17:
        n[i]=0
        n[i+1]=0
    
    

for i in n:
    if i!=0:
        c+=1
print(c)

