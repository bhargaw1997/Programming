from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        d=defaultdict(int)
        for word in words:
            if word in d.keys():
                d[word]+=1
            else:
                d[word]=1
            word_len=len(words[0])
        res=[]
        
        for i in range(len(s)-len(words)*word_len+1): 
            j=0
            while j < len(words):
                temp = s[i+j*word_len:i+j*word_len+word_len]
                if(temp in d.keys() and d[temp]!=0):
                    d[temp] -= 1
                    j+=1
                else:
                    break
            if all(x==0 for x in d.values()):
                res.append(i)
            d=defaultdict(list)
            for word in words:
                if word in d.keys():
                    d[word]+=1
                else:
                    d[word]=1
        return res
                

                        
                    