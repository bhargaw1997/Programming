class Solution:
    def countSubstrings(self, s: str) -> int:
        #base case
        if not s:
            return 0
        ans=0
        #initialize 2d array
        dp = [[False]*len(s) for _ in range(len(s))]
        
        #1 character palindrom
        for i in range(len(s)):
            dp[i][i] = True
            ans += 1
        
        #2 character palindrom
        for i in range(0,len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] =True 
                ans+=1
        
        #3 or more characters palindrom
        for length in range(2,len(s)):
            i=0
            for j in range(i+length,len(s)):
                if dp[i+1][j-1] == True and s[i] == s[j]:
                    dp[i][j] = True
                    ans+=1
                i+=1
        return ans