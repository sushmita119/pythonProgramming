l=[]
while True:
    j=input()
    if j =='q' or j=='Q':
        break
    else:
        l.append(j)
b=l.count('-')
t=len(l)
s=len(set(l))
print(b)
print(t)
print(s)
