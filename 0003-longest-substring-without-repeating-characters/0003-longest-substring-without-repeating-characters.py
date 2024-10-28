class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res =  ""
        max_length = 0
        for c in s:
            if c not in res:
                res+=c
            else:
                while c in res:
                    res = res[1:]
                res += c
            if len(res) > max_length:
                max_length = len(res)
        return max_length
