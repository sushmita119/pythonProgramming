def digit(n):
    s=0
    for i in str(n):
        s+=int(i)
    return s
n,q = map(int,input().split())
if n >= 1 and q>=1 and n<=100000 and q<= 100000:
    
    array = list(map(int,input().split()))[:n]
if all(i >= 1 and i<= 1000000000 for i in array):
        
    query =[]
    for i in range(q):
        query.append(int(input()))
    if all(i >= 1 and i<= n for i in query):
        for i in query:
            if i < len(array):
                k=array[i]
                q_digit= digit(array[i-1])
                c=0
                        
                for j in range(i,len(array)):
                    c=(i)+1
                    a_digit = digit(array[j])
                            
                    if i<k and q_digit> a_digit:
                        print(c)
                              
                        break
                else:
                    print("-1")
                        
            else:
                print("-1")



