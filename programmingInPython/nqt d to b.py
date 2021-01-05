def dtob(n):
    if(n>1):
        dtob(n//2)
    print(n%2, end=" ")
n=10
dtob(n)
