n=int(input())
s=0
tot=0
for i in str(n):
    s+=int(i)**3
if s==n:
    print("Armstrong Number")
    for i in str(n):
        if int(i)%2==0:
            tot+=int(i)
else:
    for i in str(n):
        if int(i)%2!=0:
            tot+=int(i)
print(tot)
