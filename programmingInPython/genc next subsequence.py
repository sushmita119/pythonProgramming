def subseq(s1,s2,n,m):
    
    if n==0: return True
    if m==0: return False
    if s1[n-1]==s2[m-1]:
        return(subseq(s1,s2,n-1,m-1))
    return(subseq(s1,s2,n,m-1))
s1='gesk'
s2='geeksfor'
n=len(s1)
m=len(s2)

res = subseq(s1,s2,n,m)
print(res)
