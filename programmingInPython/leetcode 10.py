num=2
num1={1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:'L',40:'XL',10:"X",9:"IX",5:'V',4:'IV',1:"I"}
string1=""
while num!=0:
    for i in num1:
        print(i)
        if num>=i:
            num-=i
            string1=string1+num1[i]
            break
print( string1)
