class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_typed = []
        t_typed = []

        for i in range(len(s)):
            if s[i] != "#":
                s_typed.append(s[i])
            elif s_typed:
                s_typed.pop()

        for i in range(len(t)):
            if t[i] != "#":
                t_typed.append(t[i])
            elif t_typed:
                t_typed.pop()

        return "".join(s_typed) == "".join(t_typed)


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def skip(s, pointer):
            skip = 0
            while pointer >= 0 and (s[pointer] == "#" or skip):
                if s[pointer] == "#":
                    skip += 1
                else:
                    skip -= 1
                pointer -= 1

            return pointer

        p1, p2 = len(s) - 1, len(t) - 1
        while p1 >= 0 or p2 >= 0:
            p1 = skip(s, p1)
            p2 = skip(t, p2)

            if p1 > -1 and p2 > -1:
                if s[p1] != t[p2]:
                    return False
                else:
                    p1 -= 1
                    p2 -= 1
            elif p1 > -1 and p2 == -1 or p1 == -1 and p2 > -1:
                return False

        return True
