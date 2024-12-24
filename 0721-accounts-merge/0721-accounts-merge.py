from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Step 1: Create email-to-account mapping
        email_to_name = {}
        graph = defaultdict(list)

        # Step 2: Build the graph
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                email = account[i]
                email_to_name[email] = name  # map email to the account name
                if i > 1:
                    graph[account[i]].append(account[i - 1])  # connect current email to previous
                    graph[account[i - 1]].append(account[i])  # and vice versa

        # Step 3: Use DFS to find all connected components (emails that belong to the same account)
        visited = set()
        result = []

        def dfs(email, component):
            visited.add(email)
            component.append(email)
            for neighbor in graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        # Step 4: Iterate through all emails and perform DFS
        for email in email_to_name:
            if email not in visited:
                component = []
                dfs(email, component)
                result.append([email_to_name[email]] + sorted(component))

        return result
