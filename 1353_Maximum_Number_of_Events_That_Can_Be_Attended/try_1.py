class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        '''
        greedy => 依照時間順序新增候選人，每次都先把最快結束的選起來
        '''
        max_time = 0
        candidates = collections.defaultdict(list)
        for start, end in events:
            candidates[start].append(end)
            max_time = max(max_time, end)
        
        count = 0
        avaliable = []
        for time in range(1, max_time+1):
            # 增加候選人
            for v in candidates[time]:
                heapq.heappush(avaliable, v)
            
            # 先把能選的選起來
            while avaliable:
                end = heapq.heappop(avaliable)
                
                if end >= time:
                    count += 1
                    break # 同一時段只能選一個
        
        return count