class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        bisect_left first => expand from center
        '''
        
        start_index = bisect.bisect_left(arr, x)
        
        i = j = start_index
        diff = 0
        while j-i <= k:
            choose_diff = float('inf')
            if i >= 0 and j < len(arr):
                if x - arr[i] <= arr[j] - x:
                    i -= 1
                else:
                    j += 1
            elif i >= 0:
                i -= 1
            else:
                j += 1
        
        return arr[i+1: j]
                            
            
