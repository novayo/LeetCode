class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        new_warehouse = []
        cur_min = float('inf')
        
        for w in warehouse:
            cur_min = min(cur_min, w)
            new_warehouse.append(cur_min)
        
        occupy = len(new_warehouse)-1
        ans = 0
        for box in sorted(boxes):
            while occupy >= 0 and box > new_warehouse[occupy]:
                occupy -= 1
            
            if occupy >= 0 and box <= new_warehouse[occupy]:
                occupy -= 1
                ans += 1
            else:
                break
        
        return ans
