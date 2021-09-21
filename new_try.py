#Kevin Naughton solution https://www.youtube.com/watch?v=PZYTs9y4f4o&t=12s
#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

class TreeNode(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

if len(nums) == 0:
    print("false")

def constructBST(nums, left, right):
    if left > right:
        return 0

    mid = left + (right - left) // 2
    cur = TreeNode(nums[mid])
    cur.left = constructBST(nums, left, mid-1)
    cur.right = constructBST(nums, mid + 1, right)
    return cur

print(constructBST(nums, 0, len(nums)-1))
