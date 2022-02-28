class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        期望拿 最先結束的出來 => 以這個標準找看有誰的「起始點」是在這個「結束點」前的
        這樣會是最佳解，因為我一次處理完所有可以處理的
        '''
        
        points.sort(key=lambda x: x[1])
        
        ans = 0
        cur_end = -float('inf')
        for a, b in points:
            if a > cur_end:
                ans += 1
                cur_end = b
        return ans                
