t=int(input())
if t>=1 and t<=20:
    
    for i in range(t):
        n=int(input())
        if n >=2 and n<=100000:
            
            left = list(map(int,input().split()))[:n]
            right = list(map(int,input().split()))[:n]
            
            t=0
            i=1
            j=n-1
            if (left[i-1]+right[i-1]) > (left[j]+right[j]):
                    t+=((left[i-1]*((i-1)) + (right[i-1]*(n-(i-1)-1)))
                    t+=((left[j]*((i+1)-1)) + (right[j]*(n-i-1)))
            i+=1
            j-=1
            print(t)
            while(i<=j):
                if (left[i]+right[i]) < (left[j]+right[j]):
                    t+=((left[i]*((i+1)-1)) + (right[i]*(n-i-1)))
                    t+=((left[j]*((i+2)-1)) + (right[j]*(n-(i+1)-1)))
                    print("l",(left[i]*((i+1)-1)))
                    print("r",(right[i]*(n-i-1)))
                else:
                    t+=((left[j]*((i+1)-1)) + (right[j]*(n-i-1)))
                    t+=((left[i]*((i+2)-1)) + (right[i]*(n-(i+1)-1)))
                    
                    print("l1",(left[j]*((i+1)-1)))
                    print("r1",(right[j]*(n-i-1)))
                    print("l2",(left[i]*((i+2)-1)))
                    print("r2",(right[i]*(n-(i+1)-1)))
                    
                i+=1
                j-=1
                print(t)
            print(t)
















































