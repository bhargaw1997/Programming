from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = Counter(s)
        for i in dic.keys():
            if(dic[i]==1):
                return s.index(i)
        return -1