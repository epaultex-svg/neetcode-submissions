# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()

        q.append(root)

        cur = root

        if not root:
            return root

        while q:

            cur = q.popleft()
            tmp = cur.right or None
            cur.right = cur.left or None
            cur.left = tmp

            if cur.right:
                q.append(cur.right)
            if cur.left:
                q.append(cur.left)


        return root