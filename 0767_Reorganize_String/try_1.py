class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)
        
        heap = []
        for w, time in counter.items():
            heapq.heappush(heap, (-time, w))
        
        ans = ''
        while len(heap) > 1:
            a_t, a_w = heapq.heappop(heap)
            b_t, b_w = heapq.heappop(heap)
            
            a_t *= -1
            b_t *= -1
            
            if not ans or ans[-1] != a_w:
                ans += (a_w+b_w)*b_t
            else:
                ans += (b_w+a_w)*b_t
            a_t -= b_t
            
            if a_t > 0:
                heapq.heappush(heap, (-a_t, a_w))
        
        if len(heap) == 1:
            a_t, a_w = heap[0]
            
            if ans and ans[-1] != a_w:
                ans += a_w
                a_t += 1
            
            i = len(ans)-1
            while i > 0:                
                if a_t == 0:
                    break
                
                if ans[i] != a_w and ans[i-1] != a_w:
                    ans = ans[:i] + a_w + ans[i:]
                    a_t += 1
                
                i -= 1
                
            if a_t != 0:
                return ""
            
        return ans
