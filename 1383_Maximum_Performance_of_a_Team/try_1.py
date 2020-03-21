class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # 在每次測試的時候，去保證現在的sum是最大的
        # 而sum由兩個因素來決定，
        # 先看右邊的元素，取min，所以若要讓這個值最大，則把efficiency由高到低去拿
        # 在看左邊的元素，是相加的，所以從現在的sum中剔除一個時（能測試下一個組合），把左邊的最小值給剃除掉（相對的右邊也要跟著剔除）
        ans = -float('inf')
        
        heap, sSum = [], 0
        pair = sorted(zip(efficiency, speed), reverse=True)
        for e, s in pair:
            if len(heap) == k:
                sSum -= heapq.heapreplace(heap, s)
            else:
                heapq.heappush(heap, s)
            sSum += s
            
            ans = max(ans, sSum * e)
        
        return ans % (10**9 + 7)
