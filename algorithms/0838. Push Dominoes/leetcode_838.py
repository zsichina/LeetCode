class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        start, cnt = 0, 0
        dominoes = ["L"] + list(dominoes) + ["R"]
        for i in range(len(dominoes)):
            if dominoes[i] == ".":
                cnt += 1
            elif dominoes[i] == "L":
                if dominoes[start] == "L":
                    for j in range(cnt):
                        dominoes[start + 1 + j] = "L"
                elif dominoes[start] == "R":
                    for j in range(cnt // 2):
                        dominoes[start + 1 + j] = "R"
                        dominoes[i - 1 - j] = "L"
                start = i
                cnt = 0
            else:
                if dominoes[start] == "R":
                    for j in range(cnt):
                        dominoes[start + 1 + j] = "R"
                start = i
                cnt = 0

        return "".join(dominoes[1:-1])


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        start, cnt = 0, 0
        dominoes = ["L"] + list(dominoes) + ["R"]
        for i in range(len(dominoes)):
            if dominoes[i] == ".":
                cnt += 1
            else:
                if dominoes[i] == dominoes[start]:
                    for j in range(cnt):
                        dominoes[start + 1 + j] = dominoes[start]
                elif dominoes[start] == "R":
                    for j in range(cnt // 2):
                        dominoes[start + 1 + j] = "R"
                        dominoes[i - 1 - j] = "L"
                start = i
                cnt = 0

        return "".join(dominoes[1:-1])
