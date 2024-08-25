class Solution(object):
    def hIndex(self, citations):
        """
        7:type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        for i, c in enumerate(citations):
            if c < i + 1:
                return i
        return i + 1
