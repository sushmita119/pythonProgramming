nums = [2,5,5,11]
target = 10
n=len(nums)
for i in range(n):
    for j in range(1,n):
        if j!=i:
            if target-nums[i]==nums[j]:
                print([j,i])
            break
        
       
