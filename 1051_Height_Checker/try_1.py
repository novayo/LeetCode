class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # sorted
        '''
        先排序，在看有幾個不同及為答案
        '''
        
        ans = 0
        sorted_heights = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                ans += 1
        return ans
