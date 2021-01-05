from itertools import combinations 
  
def rSubset(arr): 
  
    # return list of all subsets of length r 
    # to deal with duplicate subsets use  
    # set(list(combinations(arr, r))) 
    return list(combinations(arr)) 
  
# Driver Function 
arr = [1, 2, 3, 4] 
print (rSubset(arr))
