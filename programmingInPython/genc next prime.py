a=int(input())

b=int(input())

if(a<=0 or b<=0 or a>=b):

    print("Provide valid input")

else:

    while(a<=b):

        if(a==2):

            print(a,end=" ");

        elif(a==1):

            a+=1

            continue            

        else:

            flag=0

            for i in range(2,a//2+1):

                if(a%i==0):

                    flag=1

                    break

            if flag==0:

                print(a,end=" ")         

        a+=1
