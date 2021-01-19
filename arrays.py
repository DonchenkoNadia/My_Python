nums1 = [1,2]
nums2 = [3,4]
median = (len(nums1) + len(nums2))//2 + 1
res = [0]*median
for i in range(median):
    print (i)
#    if nums1[i] < nums2[i]:
        #res[i] = nums1[i]
    #else:
        #res[i] = nums2[i]
for i in range(median):
    print(res[i])
