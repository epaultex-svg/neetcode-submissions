# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        seen = set()

        while cur:
            if cur.next in seen:
                return True
            else:
                seen.add(cur)
            cur = cur.next
        return False
                
