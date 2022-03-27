class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def get(i, c):
            return abs(target - (s + i*c))
        
        arr.append(0)
        arr.sort()
        s = sum(arr)
        
        ans = float('inf')
        ans_diff = float('inf')
        
        for i in range(len(arr)-1, 0, -1):
            s -= arr[i]
            changes = len(arr) - i
            
            l, r = arr[i-1]+1, arr[i]
            while l <= r:
                mid = l + (r-l) // 2
                
                a, b, c = get(mid-1, changes), get(mid, changes), get(mid+1, changes)
                if a <= b < c:
                    r = mid - 1
                else:    
                    l = mid + 1
            
            if ans_diff >= get(l-1, changes):
                ans = l-1
                ans_diff = get(l-1, changes)
        return ans
