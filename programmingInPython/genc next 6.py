def sumd(n):
    s=0
    while(n!=0):
        
        s= s+int(n%10)
        n=int(n/10)
    return(s)
n=int(input("Enter the car number: "))
s=sumd(n)
print(s)

if len(str(n))<4 or n<0 or len(str(n))>4:
    print("Invalid input")
else:
    
    if s%3==0 or s%5==0 or s%5==0:
        print("Lucky Number")
    else:
        print("Not lucky number")


