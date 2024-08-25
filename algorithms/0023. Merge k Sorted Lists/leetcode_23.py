from heapq import heapify, heappop, heappush
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        heap: List[tuple[int, int]] = []
        heapify(heap)
        for idx, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, idx))

        curr = dummy
        while heap:
            _, idx = heappop(heap)
            curr.next = lists[idx]  # type: ignore
            curr = curr.next  # type: ignore
            if curr.next:  # type: ignore
                lists[idx] = curr.next  # type: ignore
                heappush(heap, (curr.next.val, idx))  # type: ignore

        return dummy.next
