class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        current_solution=""
        for char in s:
            if(char not in current_solution):
                current_solution+=char
            else:
                while(char in current_solution):
                    current_solution=current_solution[1:]
                current_solution+=char
            if(len(current_solution)>maxlen):
                maxlen=len(current_solution)
        return maxlen