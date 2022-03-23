class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        dic = collections.Counter(s)
        for i in t:
            if i in dic:
                dic[i]-=1
        return all(i==0 for i in dic.values())