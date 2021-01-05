import re

n=input()
temp=re.findall(r'\d+',n)
l=list(map(int,temp))
print(l)
for i in range(0,len(l)):
    for j in range(0,i):
        if j!=9:
            print(l[i])
        else:
            break
        

            
