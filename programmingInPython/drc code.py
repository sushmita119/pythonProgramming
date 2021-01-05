n=int(input())
l=[]
m=-1000
for i in range(n):
    l.append(float(input()))
for i  in range(n-4):
    s=l[i]*l[i+1]*l[i+2]*l[i+3]
    if s>m:
        m=s
print(m)

