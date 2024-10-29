from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        output = []

        if ns < np:
            return output
        
        p_count = Counter(p)
        s_count = Counter()

        for i in range(ns):
            s_count[s[i]] += 1

            if i >= np:
                if s_count[s[i-np]] == 1:
                    del s_count[s[i-np]]
                else:
                    s_count[s[i-np]] -= 1

            if s_count == p_count:
                output.append(i-np+1)
        return output