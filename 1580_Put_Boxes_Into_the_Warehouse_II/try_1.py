class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        '''
        以最小為界線，計算左邊->右邊
        最小值都包含在左邊
        '''
        n = len(warehouse)
        min_index = 0
        left = [0] * n
        right = [0] * n
        
        cur_min = float('inf')
        for i in range(n):
            if cur_min > warehouse[i]:
                min_index = i
            cur_min = min(cur_min, warehouse[i])
            left[i] = cur_min
        
        cur_min = float('inf')
        for i in range(n-1, -1, -1):
            cur_min = min(cur_min, warehouse[i])
            right[i] = cur_min
        
        
        ans = 0
        i, j = min_index, min_index+1
        for box in sorted(boxes):
            while i >= 0 or j < n:
                find_min = float('inf')
                if i >= 0:
                    find_min = min(find_min, left[i])
                if j < n:
                    find_min = min(find_min, right[j])

                if find_min == float('inf'):
                    break

                if i >= 0 and find_min == left[i]:
                    i -= 1
                    if box <= left[i+1]:
                        ans += 1
                        break
                elif j < n and find_min == right[j]:
                    j += 1
                    if box <= right[j-1]:
                        ans += 1
                        break
        return ans


