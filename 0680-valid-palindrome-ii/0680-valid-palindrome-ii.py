class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        def check_palindrom(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        
        while i < j:
            if s[i] != s[j]:
                return check_palindrom(s, i + 1, j) or check_palindrom(s, i, j -1)
            i += 1
            j -= 1
        return True
