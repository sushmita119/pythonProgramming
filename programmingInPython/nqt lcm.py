def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a,b=10,100
res=a*b//gcd(a,b)
print(res)
