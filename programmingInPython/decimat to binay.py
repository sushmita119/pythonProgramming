def dtob(n):
    i=0
    l=[0]*n
    while(n>0):
        l[i]=n%2
        n//=2
        i+=1
        
    for j in range(i-1,-1,-1):
        print(l[j],end=" ")
def btod(n):
    dec,i=0,0
    while(n>=0):
        rem=n%10
        n//=10
        dec=rem*pow(2,i)
        i+=1
    print(dec)
        
n=5
print("kkkkkkkkk")
m=101
btod(m)
dtob(n)
    
