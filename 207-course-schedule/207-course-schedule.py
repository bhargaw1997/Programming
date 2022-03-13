from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        sorted_list=[]
        if numCourses <=0:
            return False
        
        #Initialize graph and in_degree
        graph = {i:[] for i in range(numCourses)}
        in_degree = {i:0 for i in range(numCourses)}
        
        #build graph
        for i in prerequisites:
            parent,child= i[0], i[1]
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
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources.append(child)
        return len(sorted_list) == numCourses
            