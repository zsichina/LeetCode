from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        currNode = dummy
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sm = carry + x + y
            carry = sm // 10
            currNode.next = ListNode(sm % 10)
            currNode = currNode.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        if carry > 0:
            currNode.next = ListNode(carry)

        return dummy.next


# Solution N2
# class Solution:
#     def joinLinkedList(self, node: Optional[ListNode]):
#         num = 0
#         i = 0
#         while node:
#             num += node.val * 10 ** i
#             node = node.next
#             i += 1
#         return num
#
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         sm = str(self.joinLinkedList(l1) + self.joinLinkedList(l2))
#         root = ListNode(sm[-1])
#         currNode = root
#         for i in range(len(sm) - 2, -1, -1):
#             currNode.next = ListNode(sm[i])
#             currNode = currNode.next
#         return root
