def pal(s):
    i=0
    h=len(str(s))-1
    #for _ in range(len(str(s))):
    while(i<=h):
        if str(s)[i]!=str(s)[h]:
            print("not palindrome")
            break
    else:
        print("yes pal")
    i+=1
    h-=1
s=121343
pal(s)

            
