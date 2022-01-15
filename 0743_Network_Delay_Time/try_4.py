class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build table
        table = [[float('inf')] * (n+1) for _ in range(n+1)]
        
        # init
        for i in range(1, n+1):
            table[i][i] = 0
        for i, j, w in times:
            table[i][j] = w
        
        # floyd warshall
        for m in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    if table[i][j] > table[i][m] + table[m][j]:
                        table[i][j] = table[i][m] + table[m][j]
        
        # 從k走到其他所有點的最大時間
        _max = -1
        for j in range(1, n+1):
            _max = max(_max, table[k][j])
        return _max if _max != float('inf') else -1
