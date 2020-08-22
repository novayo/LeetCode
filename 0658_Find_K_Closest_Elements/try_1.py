class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search
        '''
        找到target的index後，左右再新增一個，一直新增下去，左邊先考慮（因為值比較小），直到個數==k
        左右要符合邊界才會新增以及看哪個更靠近target再去新增左或是右
        而新增可以用兩個變數去代替範圍，之後再去輸出即可
        
        注意：
        1. 可能會有相同的值，因此要找到最左邊（因為要以小的為優先）
        '''
        
        # find target's index（bisect_left）
        left, right = 0, len(arr)-1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] >= x:
                right = mid
            else:
                left = mid + 1
        
        # define two variables to locate the range of ans
        l = r = -1
        if arr[left] == x:
            l, r = left-1, left+1
        else:
            l, r = left-1, left
        
        while r-l <= k:
            if l < 0:
                r += 1
                continue
            
            if r >= len(arr):
                l -= 1
                continue
            
            if abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1
            
        return arr[l+1:r]
        
