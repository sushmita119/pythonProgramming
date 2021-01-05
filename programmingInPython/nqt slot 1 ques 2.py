n=10
can=int(input())
if can > n or can <=0:
    print("Invalid Input")
    print("Number of candies available:",n)

    
else:
    print("Number of Candies sold:",can)
    print("Number of candies available:",n-can)
