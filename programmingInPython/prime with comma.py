n=50
l=[]
for i in range(n+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                l.append(str(j))
print(",".join(l))
