from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        character_size = 0
        for num in data:
            num = f'{num:08b}'
            if character_size == 0:
                if num.startswith("11111") or num.startswith("10"):
                    return False
                elif num.startswith("11110"):
                    character_size = 3
                elif num.startswith("1110"):
                    character_size = 2
                elif num.startswith("110"):
                    character_size = 1
            else:
                if num.startswith("10"):
                    character_size -= 1
                else:
                    return False

        return character_size == 0
