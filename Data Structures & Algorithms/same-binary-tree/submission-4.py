# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        s = [p]


        pNodes = [p.val] if p else None
        qNodes = [q.val] if q else None

        while s:
            node = s.pop()

            if node:
                if node.left:
                    s.append(node.left)
                    pNodes.append(node.left.val)
                if node.right:
                    if not node.left:
                        s.append(None)
                        pNodes.append(None)
                    s.append(node.right)
                    pNodes.append(node.right.val)

        s = [q]

        while s:
            node = s.pop()

            if node:
                if node.left:
                    s.append(node.left)
                    qNodes.append(node.left.val)
                if node.right:
                    if not node.left:
                        s.append(None)
                        qNodes.append(None)
                    s.append(node.right)
                    qNodes.append(node.right.val)

        print((pNodes,qNodes))

        return pNodes == qNodes

                    
