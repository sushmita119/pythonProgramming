n=list(map(str,input().split()))
v=['a','e','i','o','u']
a,b="",""
for i in n[0]:
    if i in v:
        i='%'
        a+=i
    else:
        a+=i
for i in n[1]:
    if i not in v:
        i='#'
        b+=i
    else:
        b+=i
print(a+b+n[2].upper())
        
