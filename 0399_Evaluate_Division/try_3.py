class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # graph
        index_table = {}
        index_list = []
        graph = collections.defaultdict(list)
        for i, (a, b) in enumerate(equations):
            value = values[i]
            
            if a not in index_table:
                index_table[a] = len(index_table)
                index_list.append(a)
            if b not in index_table:
                index_table[b] = len(index_table)
                index_list.append(b)
            
            graph[a].append((value, b))
            graph[b].append((1/value, a))
        
        # init
        table = [[float('inf')] * len(index_table) for _ in range(len(index_table))]
        for i in range(len(index_table)):
            table[i][i] = 1
        for i, (a, b) in enumerate(equations):
            value = values[i]
            index_a = index_table[a]
            index_b = index_table[b]
            table[index_a][index_b] = value
            table[index_b][index_a] = 1/value
        
        # floyd warshall
        for a in index_list:
            for b in index_list:
                for c in index_list:
                    index_a = index_table[a]
                    index_b = index_table[b]
                    index_c = index_table[c]
                    
                    if table[index_b][index_a] != float('inf') and table[index_a][index_c] != float('inf'):
                        table[index_b][index_c] = table[index_b][index_a] * table[index_a][index_c]
        
        # find ans
        ans = []
        for a, b in queries:
            if a not in index_table or b not in index_table:
                ans.append(-1)
            else:
                index_a = index_table[a]
                index_b = index_table[b]
                if table[index_a][index_b] == float('inf'):
                    ans.append(-1)
                else:
                    ans.append(table[index_a][index_b])
        return ans
