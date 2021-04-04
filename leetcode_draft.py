"""
       value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)
public class MedianOfTwoSortedArrayOfDifferentLength {

    public double findMedianSortedArrays(int input1[], int input2[]) {
        //if input1 length is greater than switch them so that input1 is smaller than input2.
        if (input1.length > input2.length) {
            return findMedianSortedArrays(input2, input1);
        }
"""
nums1 = [1,3,8,9,15]
nums2 = [7,11,18,19,21,25]
x = len(nums1)
y = len(nums2)

low = 0
high = x
while low >= high:
    partitionX = (low + high)//2
    partitionY = (x + y + 1)//2 - partitionX

    #if partitionX is 0 it means nothing is there on left side. Use -INF for maxLeftX
    #if partitionX is length of input then there is nothing on right side. Use +INF for minRightX
    maxLeftX = -(2 ** 31) if partitionX == 0 else nums1[partitionX - 1]
    minRightX = (2 ** 31 - 1) if partitionX == x else nums1[partitionX]

    maxLeftY = -(2 ** 31) if partitionY == 0 else nums2[partitionY - 1]
    minRightY = (2 ** 31 - 1) if partitionY == y else nums2[partitionY]

    if maxLeftX <= minRightY and maxLeftY <= minRightX:
        #We have partitioned array at correct place
        #Now get max of left elements and min of right elements to get the median in case of even length combined array size
        #or get max of left for odd length combined array size.
        if (x + y) % 2 == 0:
            print ((max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2)
            break
        else:
            print (max(maxLeftX, maxLeftY))
            break

    elif maxLeftX > minRightY:
        #we are too far on right side for partitionX. Go on left side.
        high = partitionX - 1
    else:
        #we are too far on left side for partitionX. Go on right side.
        low = partitionX + 1
