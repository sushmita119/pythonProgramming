def fibo(n):
    n1,n2=0,1
    c=0
    while(c<n):
        print(n1,end=" ")
        s=n1+n2
        n1=n2
        n2=s
        c+=1

n=6
fibo(n)
