class Solution:
    def isSelfCrossing(self, arr: List[int]) -> bool:
        # O(n) time / O(1) space
        n = len(arr)
        solution = 2
        
        # i < 3
        if n <= 3:
            return False
        
        # i == 3
        if arr[2] <= arr[0]:
            solution = 1
            if arr[3] >= arr[1]:
                return True
        
        # i >= 4
        for i in range(4, n):
            if solution == 2:
                if arr[i-1] < arr[i-3] - (arr[i-5] if i > 4 else 0):
                    solution = 1
                    if arr[i] >= arr[i-2]:
                        return True
                elif arr[i-3] >= arr[i-1] >= arr[i-3] - (arr[i-5] if i > 4 else 0):
                    solution = 1
                    if arr[i] >= arr[i-2] - arr[i-4]:
                        return True
                    
            # solution 1
            else:
                if arr[i] >= arr[i-2]:
                    return True
        return False