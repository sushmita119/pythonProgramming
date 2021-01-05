def count_num(l,r):
    c=0
    num=0
    for i in range(l,r):
        if i!=num:
            num+=i
            c+=1
    if c>0:
        print(c)
    else:
        print("no unique no")
l,r= map(int,input().split())
count_num(l,r)
        
