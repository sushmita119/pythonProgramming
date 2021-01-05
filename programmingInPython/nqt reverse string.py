'''def rev(s):
    print(s[::-1])
s=input()
rev(s)'''
def rev(s):
    for _ in range(len(s)//2):
        i=0
        j=len(s)-1
        s1=list(s)
        s1[i],s1[j]=s1[j],s1[i]
        i+=1
        j-=1
    print(*s1)
s="book"
rev(s)
        
