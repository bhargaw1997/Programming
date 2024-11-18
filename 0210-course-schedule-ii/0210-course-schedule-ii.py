class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        sorted_list=[]
        
        if numCourses <= 0:
            return []
        
        #Initialize graph and in_degree
        graph = {i:[] for i in range(numCourses)}
        in_degree = {i:0 for i in range(numCourses)}
        
        #build graph
        for i in prerequisites:
            parent,  child = i[1], i[0]
            graph[parent].append(child)
            in_degree[child] += 1
        
        #Find all sources
        sources = deque()
        for key in in_degree:
            if in_degree[key] == 0:
                sources.append(key)
                
        #sort
        while sources:
            vertex = sources.popleft()
            sorted_list.append(vertex)
            for child in graph[vertex]:
                in_degree[child]-=1
                if in_degree[child] == 0:
                    sources.append(child)
        if len(sorted_list) == numCourses:
            return sorted_list
        else:
            return []