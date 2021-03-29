class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        from collections import deque

        left = deque()
        right = 0

        for ch in S:
            if ch == "(":
                left.append(ch)
            elif ch == ")" and left:
                left.pop()
            else:
                right += 1
        return (right + len(left))
