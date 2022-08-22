from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        fast, slow = dummy.next, dummy
        cnt = 1
        while fast.next:
            fast = fast.next
            cnt += 1
            if cnt > n:
                slow = slow.next

        slow.next = slow.next.next

        return dummy.next
