class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        arr = []
        ans = []
        
        for a, b in paint:
            s = bisect.bisect_left(arr, a)
            e = bisect.bisect_right(arr, b)
            
            _slice = []
            _sum = 0
            if s == e and s % 2 == 0:
                _sum += b-a
            
            if s % 2 == 0:
                _slice.append(a)
                if s != e:
                    _sum += arr[s] - a
            
            if e % 2 == 0:
                _slice.append(b)
                if s != e:
                    _sum += b - arr[e-1]
            
            for i in range(s//2*2+1, e-1, 2):
                _sum += arr[i+1] - arr[i]
            
            ans.append(_sum)
            arr[s:e] = _slice
        
        return ans
        
        