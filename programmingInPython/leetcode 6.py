s="PAYPALISHIRING"
numRow=3
change=-1
row=0
res=[[] for i in range(numRow)]
print(res)
if numRow<=1:
    print(s)
else:
    for c in s:
        res[row].append(c)
        if row==0 or row==numRow-1:
            change*=-1
        row+=change
    for i in range(len(res)):
        res[i]="".join(res[i])
    print("".join(res))
