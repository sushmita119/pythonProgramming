s=input()
n=len(n)
for i in range(0,n-2,2):
    if s[i+1]=='A':
        if s[i]==0 or s[i+2]==0:
            s[i+2]=0
        else:
            s[i+2]=1
            
    elif s[i+1]=='B':
        if s[i]==1 or s[i+2]==1:
            s[i+2]=1
        else:
            s[i+2]=0
    elif s[i+1]=='C':
        if s[i]==s[i+2]:
            s[i+2]=0
        else:
            s[i+2]=1
        
res=s[n-1]-0
print(res)
        
    
        
    
