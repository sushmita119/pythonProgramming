a=int(input())
n=int(input())
l=list(map(int,input().split()))[:n]
s=""
s=s.join(l)
print(s)


s=""
for i in l:
    s+=str(i)
    print(s)

t=(a**int(s))%1337

print(t)

