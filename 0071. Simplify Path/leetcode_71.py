class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for word in path.split("/"):
            if word and word != ".":
                if word == "..":
                    if res:
                        res.pop()
                else:
                    res.append(word)

        return "/" + "/".join(res)
