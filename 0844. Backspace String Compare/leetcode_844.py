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


