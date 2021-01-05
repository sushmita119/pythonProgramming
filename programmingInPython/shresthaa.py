s=input()
c=0
ans=0
if(len(s))>20:
    print("Wrong Input")
else:
    for i in s:
        if s.count(i)==1:
            print(i)
            break
    
