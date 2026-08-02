# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        s = [root]
        vals = []

        while s:
            node = s.pop()
            vals.append(node.val)

            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
        
        vals.sort()

        return (vals[k - 1])
            
