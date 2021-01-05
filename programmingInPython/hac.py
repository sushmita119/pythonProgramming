for _ in range(int(input())):
    l=[]
    plain = input()
    enc = input()
    i=0
    j=0
    while(i<len(plain) and j<len(enc)):
        diff = ord(enc[j])-ord(plain[i])
        print(diff)
        if diff<0:
            diff = diff+26
            print(diff)
    
            
            
        l.append(diff)
        i+=1
        j+=1
            
    print(l)
    s=set(l)
    if len(s)==1:
        print(*s)
    else:
        print("-1")
