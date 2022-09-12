from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        start, end = 0, len(tokens)-1
        score, max_score = 0, 0
        while start <= end:
            if power >= tokens[start]:
                power -= tokens[start]
                start += 1
                score += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[end]
                score -= 1
                end -= 1
            else:
                return max_score

        return max_score
