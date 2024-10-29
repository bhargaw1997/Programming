from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ns, np = len(s2), len(s1)
        output = False

        if ns < np:
            return output
        
        p_count = Counter(s1)
        s_count = Counter()

        for i in range(ns):
            s_count[s2[i]] += 1

            if i >= np:
                if s_count[s2[i-np]] == 1:
                    del s_count[s2[i-np]]
                else:
                    s_count[s2[i-np]] -= 1

            if s_count == p_count:
                return True
        return output