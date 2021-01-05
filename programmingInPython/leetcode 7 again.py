x=120
y=0

sign="+"
if x<0:
    sign="-"
    x=abs(x)
while x>0:
    y=y*10 + x%10
    x=x//10
    print(y)

if sign=="-":
    y=-y
print(y)

