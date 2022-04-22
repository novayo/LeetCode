class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        index = {}
        for i, bulb in enumerate(bulbs):
            index[bulb] = i+1
        
        ans = float('inf')
        
        stack = []
        for bulb_i in range(1, len(bulbs)+1):
            while stack and index[stack[-1]] > index[bulb_i]:
                bulb_j = stack.pop()
                if abs(bulb_i - bulb_j) - 1 == k:
                    ans = min(ans, max(index[bulb_i], index[bulb_j]))
                
            if stack:
                bulb_j = stack[-1]
                if abs(bulb_i - bulb_j) - 1 == k:
                    ans = min(ans, max(index[bulb_i], index[bulb_j]))
                    
            stack.append(bulb_i)
        
        return ans if ans < float('inf') else -1

# [0,0,0,0,1,1,0,1,0,0]
