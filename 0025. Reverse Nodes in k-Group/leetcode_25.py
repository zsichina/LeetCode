from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        arr = []
        curr = head
        for i in range(k):
            if not curr:
                arr = arr[::-1]
                break
            arr.append(curr)
            curr = curr.next
            arr[-1].next = None

        head = arr.pop()
        curr1 = head
        for i in range(len(arr)):
            curr1.next = arr.pop()
            curr1 = curr1.next

        if curr:
            curr1.next = self.reverseKGroup(curr, k)

        return head
