class Solution:
    def isPalindrome(self, s: str) -> bool:
        palin=""
        lower_s = s.lower()
        for ch in lower_s:
            if((ch>='a' and ch<= 'z') or (ch>='A' and ch<='Z') or (ch>='0' and ch<='9')):
                palin += ch
        # print(palin,palin[-1::-1])
        return True if palin == palin[-1::-1] else False