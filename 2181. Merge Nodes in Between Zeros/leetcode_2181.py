# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currNode = head.next
        first = head
        while currNode:
            if currNode.val !=0:
                first.val+=currNode.val
            else:
                if not currNode.next:
                    first.next = None
                    break
                first = first.next
                first.val=0
            currNode=currNode.next
        return head
