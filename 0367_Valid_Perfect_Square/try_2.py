class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        '''
        binary search
        
        去測試答案即可
        範圍是1~num//2
        '''
        if num == 1:
            return True
        
        left, right = 1, num
        while left < right:
            mid = left + (right - left) // 2
            mid2 = mid * mid
            if mid2 == num:
                return True
            elif mid2 > num:
                right = mid
            else:
                left = mid + 1
        return False
