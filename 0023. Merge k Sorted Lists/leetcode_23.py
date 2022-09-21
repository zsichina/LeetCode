from typing import List, Optional
from heapq import heapify, heappush, heappop


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        heap = []
        heapify(heap)
        for idx, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, idx))

        curr = dummy
        while heap:
            val, idx = heappop(heap)
            curr.next = lists[idx]
            curr = curr.next
            if curr.next:
                lists[idx] = curr.next
                heappush(heap, (curr.next.val, idx))

        return dummy.next
