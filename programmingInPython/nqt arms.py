def arm(n):
    s=0
    t=n
    for i in str(t):
        s+=int(i)**3
    if s==n:
        print(s,end=" ")
n=10
h=1000
for i in range(n,h+1):
    arm(i)
