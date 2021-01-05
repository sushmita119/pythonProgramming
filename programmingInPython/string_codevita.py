for _ in range(int(input())):
    res=""
    s=input()
    p=input()
    for i in s:
        if i in p:
            res+=i
    print(res)
