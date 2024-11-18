class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        sorted_list = []

        #a. initialize graph and in_degree hash table
        graph = {i:[] for i in range(numCourses)}
        in_degree = {i: 0 for i in range(numCourses)}

        #b. create graph
        for prerequisite in prerequisites:
            parent, child = prerequisite[0], prerequisite[1]
            graph[parent].append(child)
            in_degree[child] += 1
        
        #c. Find all sources:
        source = deque()
        for key in in_degree:
            if in_degree[key] == 0:
                source.append(key)
        
        #d.sort
        while source:
            vertex = source.popleft()
            sorted_list.append(vertex)
            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    source.append(child)

        return len(sorted_list) == numCourses


