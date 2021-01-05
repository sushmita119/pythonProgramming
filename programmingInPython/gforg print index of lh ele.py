
a=[40,8,50,100,200,90,1]
lar=0
for i in range(len(a)):
    if a[i]>lar:
        lar=a[i]
for i in range(len(a)):
    if a[i]==lar:
        print(i)
        break
MY CODE
'''

a=[40,8,50,100,200,90,1]
for i in range(len(a)):
    sign=True
    for j in range(len(a)):
        if a[j]>a[i]:
            sign=False
            break
    if  sign==True:
        print(i)
    
 '''   

