l=[]
for _ in range(9):
    
    i=int(input())
    if i >=1 and i<=100:
        l.append(i)
t1=l[0]+l[3]+l[6]
t2=l[1]+l[4]+l[7]
t3=l[2]+l[5]+l[8]
t11=round(t1/3)
t22=round(t2/3)
t33=round(t3/3)
if t11<70 and t22<70 and t33<70:
    
     print("Trinees unfit")
else:
    if t11>= t22 and t11>=t33:
        print("Trainee number: 1")
    if t22>= t11 and t22>=t33:
        print("Trainee number: 2")
    if t33>= t22 and t33>=t11:
        print("Trainee number: 3")
        

    


