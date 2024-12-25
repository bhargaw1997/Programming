class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        n =max(len(word1), len(word2))
        for i in range(n):
            if i < len(word1):
                ans += word1[i]
            if i < len(word2):
                ans += word2[i]
        return "".join(ans)