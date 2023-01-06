from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        curr = head
        n = 1
        while curr.next:
            n += 1
            curr = curr.next
        k %= n

        node = head
        for _ in range(n - k - 1):
            node = node.next

        curr.next = head
        new_head = node.next
        node.next = None

        return new_head
