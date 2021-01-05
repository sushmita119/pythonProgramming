def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
n,r=5,0
ncr=fact(n)//(fact(r)*fact(n-r))
npr=fact(n)//fact(n-r)
print(str(n)+"c"+str(r),ncr)
print(str(n)+"p"+str(r),npr)
