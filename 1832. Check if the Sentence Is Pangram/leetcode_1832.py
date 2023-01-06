from collections import Counter


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        counter = Counter(sentence)

        for i in range(26):
            if chr(ord("a") + i) not in counter:
                return False

        return True


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = 0

        for curr_char in sentence:
            mapped_index = ord(curr_char) - ord("a")

            curr_bit = 1 << mapped_index

            seen |= curr_bit

        return seen == (1 << 26) - 1
