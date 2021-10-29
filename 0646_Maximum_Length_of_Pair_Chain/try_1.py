class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # sort and find prev
        pairs.sort()
        dp = [1] * len(pairs)
        heap = [] # (dp, start, end)
        
        for i in range(len(pairs)):
            tmp = []
            while heap and pairs[i][0] <= heap[0][2]:
                tmp.append(heapq.heappop(heap))

            if heap:
                dp[i] = -heap[0][0] + 1

            while tmp:
                heapq.heappush(heap, tmp.pop())

            heapq.heappush(heap, (-dp[i], pairs[i][0], pairs[i][1]))
    
        return dp[-1]
