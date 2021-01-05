def shift(lis):
    c=0
    for i in range(len(lis)):
        if lis[i]!=0:
            lis[c],lis[i]=lis[i],lis[c]
            c+=1

n=int(input())
l=list(map(int,input().split()))[:n]
shift(l)
print(l)
