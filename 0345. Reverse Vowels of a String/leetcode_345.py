class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = list(s)
        vowels = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
        start, end = 0, len(lst)-1
        while start < end:
            if lst[start] not in vowels:
                start += 1
            elif lst[end] not in vowels:
                end -= 1
            else:
                lst[start], lst[end] = lst[end], lst[start]
                start += 1
                end -= 1

        return "".join(lst)
