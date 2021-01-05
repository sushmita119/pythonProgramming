def prime(n):
    c=0
    if n<=1:
        print("false")
    else:
        for i in range(2,n+1):
            if n%i==0:
                c+=1
            if c>2:
                print("False")
                break
            else:
                print("true")
                break
n=8
prime(n)
