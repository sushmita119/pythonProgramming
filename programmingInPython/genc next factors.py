n=abs(int(input()))
if n==0:
    print("No factors")
else:
    for i in range(1,n+1):
        if n%i==0:
            if i!=n:
                print(i,",",end="")
            else :
                print(i)
