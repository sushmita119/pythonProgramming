s="-91283472332"
s2=""
for i in s:
    if s2=="":
        if i==" ":
            continue
        elif i=="+" or i=="-":
            s2+=i
        elif i.isdigit()==False:
            print(0)
            break
        elif i.isdigit():
            s2+=i
    else:
        if i.isdigit():
            s2+=i
        else:
            break
print(s2)
if s2=="":
    print(0)
elif s2=="-" or s2=="+":
    print(0)
else:
    num = int(s2)
    if num <= -2**31:
        print( -2**31)
    elif num >= (2**31-1):
        print (2**31-1)
    else:
        print(num)
