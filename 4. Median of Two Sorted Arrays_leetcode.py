nums1 = [1,3]
nums2 = [2]
nums3=nums1+nums2
nums3.sort()
l=len(nums3)
if(l%2 != 0):
    print(float(nums3[l//2 ]))
else:
    c=l//2
    print( (nums3[c]+nums3[c-1])/2 )

