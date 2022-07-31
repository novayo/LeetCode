class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        arr = []
        ans = []
        
        for a, b in paint:
            s = bisect.bisect_left(arr, a)
            e = bisect.bisect_right(arr, b)
            
            _sum = 0
            tmp = []
            if s == e and s % 2 == 0:
                _sum += b-a
            
            if s % 2 == 0:
                tmp.append(a)
                
                if s != e:
                    _sum += arr[s] - a
            
            if e % 2 == 0:
                tmp.append(b)
                
                if s != e:
                    _sum += b - arr[e-1]
            
            for i in range(s//2*2+1, e-1, 2):
                _sum += arr[i+1] - arr[i]
            
            ans.append(_sum)
            arr[s:e] = tmp
        
        return ans