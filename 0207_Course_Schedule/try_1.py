class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 單向連接 找是否有cycle
        graph = collections.defaultdict(list)
        for i, j in prerequisites:
            graph[i].append(j)
        
        
        def dfs(node, color = set()):
            if node in color:
                return True
            color.add(node)
            for next_node in graph[node]:
                if dfs(next_node, color):
                    return True
            color.remove(node)
            return False
        
        for node in range(numCourses):
            if dfs(node):
                return False
        return True
        
