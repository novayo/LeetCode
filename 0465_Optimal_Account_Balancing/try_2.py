class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        graph = collections.defaultdict(int)
        for a, b, c in transactions:
            graph[a] -= c
            graph[b] += c
        
        return self.dfs(0, list(graph.values()))
    
    def dfs(self, idx, array):
        if idx >= len(array):
            return 0
        
        if array[idx] == 0:
            return self.dfs(idx+1, array)
        
        cur = array[idx]
        ret = float('inf')
        for i in range(idx+1, len(array)):
            if (array[idx] > 0 and array[i] > 0) or (array[idx] < 0 and array[i] < 0):
                continue
            
            if array[idx] == 0 or array[i] == 0:
                continue
            
            array[i] += cur
            ret = min(ret, self.dfs(idx+1, array))
            array[i] -= cur
        return ret + 1
        
        