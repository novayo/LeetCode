class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        '''
        move all chips to 1 or 2 first
        and check out which one is smaller one
        奇數=1，偶數=2
        '''
        
        counter = {1: 0, 2: 0}
        for chip in position:
            if chip % 2 == 0:
                counter[2] += 1
            else:
                counter[1] += 1
        
        return min(counter[1], counter[2])
