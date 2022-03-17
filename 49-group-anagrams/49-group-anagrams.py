from collections import defaultdict,Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_lst = []
        for i in strs:
            word=sorted(i)
            new_lst.append("".join(word))
        dic = defaultdict(list)
        for i,a in enumerate(new_lst):
            if a not in dic.keys():
                dic[a] = [strs[i]]
            else:
                dic[a].append(strs[i])
        ans=[]
        for i in dic.keys():
            ans.append(dic[i])
        return ans