class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = bisect.bisect_left(arr, x)
        ans = collections.deque()
        
        left = index - 1
        right = index
        while len(ans) < k:
            l = x - arr[left] if left >= 0 else float('inf')
            r = arr[right] - x if right < len(arr) else float('inf')
            
            if l <= r:
                ans.appendleft(arr[left])
                left -= 1
            else:
                ans.append(arr[right])
                right += 1
        return ans
