class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        
        for email in emails:
            name,domain = email.split('@')
            local = name.split('+')[0].replace('.','')
            uniqueEmails.add(local+'@'+domain)
        return len(uniqueEmails)
    
# Let NN be the number of the emails and MM be the average length of an email.

# Time Complexity: O(N \cdot M)O(N⋅M)
    # The split method must iterate over all of the characters in each email and the replace method must iterate over all of the characters in each local name. As such, they both require linear time and are O(M)O(M) operations. Since there are N emails and the average email has M characters in it, the complexity is of order (Number of emails) * (Number of characters in an email) = N*M.

# Space Complexity: O(N \cdot M)O(N⋅M)
    # In the worst case, when all emails are unique, we will store every email address given to us in the hash set.

