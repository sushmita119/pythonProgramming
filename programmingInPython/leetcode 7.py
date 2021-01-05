
def eliminate(x):
    x=str(x)
    x_list=list(x)
    if x_list[-1] == "0":
        x_new=x_list[:(len(x_list)-1)]
        x_join="".join(x_new)
        return((x_join))
    else:
        return(x)
def rev(z):
    z_rev=z[::-1]
    return(z_rev)
y=-123
if y<=1:
    print(y)
else:
    num=eliminate(y)
    num_rev=list(rev(num))
    if "-" in num_rev:
        num_new=num_rev[:(len(num_rev)-1)]
        num_join="".join(num_new)
        reversed_=("-"+num_join)
        print(reversed_)
    else:
        print(rev(num))
    







   


