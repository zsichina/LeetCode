from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        character_size = 0
        for num in data:
            num = f"{num:08b}"
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


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        bits_left = 0
        for num in data:
            bit_num = f"{num:08b}"
            if bits_left == 0:
                if bit_num.startswith("0"):
                    continue

                for bit in bit_num:
                    if bit == "0":
                        break
                    bits_left += 1

                if not (1 < bits_left < 5):
                    return False
            else:
                if not bit_num.startswith("10"):
                    return False
            bits_left -= 1

        return bits_left == 0
