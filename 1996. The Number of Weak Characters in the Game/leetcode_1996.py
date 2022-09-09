from typing import List
from heapq import heapify, heappush, heappop

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        start, end, n, res = 0, 0, len(properties), 0
        
        heapify(properties)
        max_heap = []
        heapify(max_heap)
        for attack, defence in properties:
            heappush(max_heap, (-defence, -attack))
            
        while properties and max_heap:
            attack, defence = heappop(properties)
            while max_heap and -max_heap[0][1] <= attack:
                heappop(max_heap)
            
            if max_heap and -max_heap[0][0] > defence:
                res += 1
                
        return res
