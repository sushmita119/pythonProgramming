'''
def binaryS(l,x):
    low = 0
    high = len(l)-1
    mid=0
    while(low<=high):
        mid = (low+high)//2
        if l[mid]> x:
            high = mid-1
        elif l[mid]<x:
            low = mid+1
        else:
            return mid
'''
def prime(n):
    if n<=1:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
                
        else:
            return True
def rev(l,n):
    l=list(l)
    low=0
    h=n-1
    while(low<=h):
        l[low],l[h]=l[h],l[low]
        low+=1
        h-=1
    return l
l="sushmita" 
#n=6
#result = binaryS(l,n)
#print(result)
'''
if prime(n):
    
    print("Prime")
else:
    print("Not Prime")
'''
res=rev(l,len(l))
print("".join(res))
