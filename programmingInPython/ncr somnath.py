for _ in range(int(input())):
    length=int(input())
    l=list(map(int,input().split()))[:length]
    m,n=sum(l)-(sum(l)//2),sum(l)//2
    print("ANS ", m-n)
