from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code_map = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
        ]
        transformed_words = set()
        offset = ord("a")
        for word in words:
            transformed_word = ""
            for letter in word:
                idx = ord(letter) - offset
                transformed_word += morse_code_map[idx]
            transformed_words.add(transformed_word)

        return len(transformed_words)


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code_map = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
        ]

        transformed_words = {
            "".join(morse_code_map[ord(l) - ord("a")] for l in w) for w in words
        }

        return len(transformed_words)

