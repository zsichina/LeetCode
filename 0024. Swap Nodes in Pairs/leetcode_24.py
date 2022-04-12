from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        if head and head.next:
            temp = head
            head = head.next
            temp.next = temp.next.next
            head.next = temp

        if head.next and head.next.next:
            head.next.next = self.swapPairs(head.next.next)

        return head
