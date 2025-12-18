# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        b=""
        cur = head
        while cur:
            b+=str(cur.val)
            cur = cur.next
        return int(b,2)
        
