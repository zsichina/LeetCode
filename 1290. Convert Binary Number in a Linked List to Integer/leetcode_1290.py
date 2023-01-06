class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        total = 0
        curr = head
        while curr:
            total = total * 2 + curr.val
            curr = curr.next

        return total


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        total = 0
        curr = head
        while curr:
            total *= 2
            total |= curr.val
            curr = curr.next

        return total


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        total = 0
        curr = head
        while curr:
            total = (total << 1) | curr.val
            curr = curr.next

        return total
