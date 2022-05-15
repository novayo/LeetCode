class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        '''
        init => idx=0 Monday
        每周一飛一次
        
        flight 只是能不能飛而已
        day[地i個地方][第j周] = 可以放假幾天
        
        最多100周，100個航班
        '''
        graph = collections.defaultdict(list)
        for i, f in enumerate(flights):
            for j in range(len(f)):
                if f[j] == 1:
                    graph[i].append(j)
        
        memo = {}
        def dfs(i, d):
            if d >= len(days[0]):
                return 0
            
            if (i, d) not in memo:
                ret = 0

                # stay
                ret = max(ret, dfs(i, d+1) + days[i][d])

                # next place
                for j, avaliable in enumerate(flights[i]):
                    if avaliable:
                        ret = max(ret, dfs(j, d+1) + days[j][d])
                
                memo[i, d] = ret
                
            return memo[i, d]
        
        return dfs(0, 0)