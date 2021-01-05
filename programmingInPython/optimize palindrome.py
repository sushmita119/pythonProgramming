def pal(n,l,h):
    while(l<h):
        if(str(n)[l]!=str(n)[h]):
            return False
        l+=1
        h-=1
    return True
n=1787909
l,h=0,len(str(n))-1
res=pal(n,l,h)
if res:
    print("Palindrome")
else:
    print("Not Palinfrome")
