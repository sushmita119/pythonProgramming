s="bb"
l={}
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        temp=s[i:j]
        if temp==temp[::-1]:
            l[temp]=len(temp)
print(l)
c=0
def get_key(val):
    for key,value in l.items():
        if val==value:
            return key
        
for i in l.values():
    if i>c:
        c=i
print(get_key(c))
    
    
        
