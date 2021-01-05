s ="pwwkew"
c=0
l=[]
for i in range(len(s)):
    if s[i] not in l:
        l.append(s[i])
        c+=1
print(c)
print(l)
