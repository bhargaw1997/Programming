class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_bracket = 0
        min_adds = 0

        for i in s:
            if i == '(':
                open_bracket += 1
            else:
                if open_bracket > 0:
                    open_bracket -= 1
                else: 
                    min_adds += 1
        return open_bracket + min_adds