class Solution:
  def isValid(self, s: str) -> bool:
    if len(s)%2 != 0: return
    stack = []
    open = "([{"
    close = ")]}"
    for c in s:
      if c in open:
        stack.append(c)
      elif len(stack) == 0 or c != close[open.find(stack.pop())]:
        return False
    return len(stack) == 0
