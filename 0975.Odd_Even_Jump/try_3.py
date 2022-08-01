from sortedcontainers import SortedList
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        '''
        odd => 跳下一個略大 => maintain bst => bisect.bisect_left
        even => 跳下一個略小 => maintain bst => (neg) bisect.bisect_left
        
        [10,13,12,14,15]
    odd   F  F  F  T  T
    even  F  F  F  F  T
        '''
        n = len(arr)
        dp = [[False, False] for _ in range(n)]
        bigger = SortedList()
        smaller = SortedList()
        
        dp[-1][0] = dp[-1][1] = True
        bigger.add((arr[-1], n-1))
        smaller.add((-arr[-1], n-1))
        
        for i in range(n-2, -1, -1):
            val = arr[i]
            b = bigger.bisect_left((val,))
            s = smaller.bisect_left((-val,))
            
            # odd
            if b < len(bigger):
                bigger_val, bigger_index = bigger[b]
                dp[i][0] = dp[bigger_index][1]
            
            # even
            if i > 0 and s < len(smaller):
                smaller_val, smaller_index = smaller[s]
                dp[i][1] = dp[smaller_index][0]
            
            bigger.add((val, i))
            smaller.add((-val, i))
        
        return sum([dp[i][0] for i in range(n)])
