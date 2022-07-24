from collections import defaultdict
import heapq

class NumberContainers:

    def __init__(self):
        self.number_container = {}
        self.num_index_set = defaultdict(set)
        self.num_index_heap = defaultdict(list)


    def change(self, index: int, number: int) -> None:
        if index not in self.number_container:
            self.number_container[index] = number
            self.num_index_set[number].add(index)
            heapq.heappush(self.num_index_heap[number], index)
        else:
            self.num_index_set[self.number_container[index]].remove(index)

            self.number_container[index] = number
            self.num_index_set[number].add(index)
            heapq.heappush(self.num_index_heap[number], index)

            
    def find(self, number: int) -> int:
        
        while self.num_index_heap[number]:
            if self.num_index_heap[number][0] in self.num_index_set[number]:
                return self.num_index_heap[number][0]
            
            heapq.heappop(self.num_index_heap[number])
        
        return -1


