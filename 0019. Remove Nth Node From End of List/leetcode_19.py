from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        currNode = head
        currNode2 = head

        i = 0
        while True:
            if currNode.next is None:
                if n == 1 and i == 0:
                    return None
                elif i == n-1:
                    return currNode2.next
                else:
                    currNode2.next = currNode2.next.next
                    return head
            currNode = currNode.next

            if i > n-1:
                currNode2 = currNode2.next
            i+=1

        return head
