nums1 = [1,3]
nums2 = [2]
nums1 = nums1 + nums2
nums1.sort()
if (len((nums1)))&1 ==0:
   print((nums1[len(nums1)//2]+nums1[len(nums1)//2-1])/2)
else:
    print(nums1[len(nums1)//2])
