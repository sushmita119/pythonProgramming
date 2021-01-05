print("Enter The Salary")
s=int(input())
print("Enter the preferial")
p=float(input())
if s<0  or p <1 or  p>5:
    print("Invalid Input")
else:
    if p>=1 and p<=3:
        t=s+(s*0.1)
    elif p>=3.1 and p<=4:
        t=s+(s*0.25)
    elif p>=4.1 and p<=5:
        t=s+(s*0.3)
    print(int(t))
    
    
    
