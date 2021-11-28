class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        crack = collections.defaultdict(int)
        
        # 計算最多跨過幾面牆
        height = len(wall)
        
        # 計算裂縫
        for row in wall:
            sum_up = 0
            for value in row[:-1]:
                sum_up += value
                crack[sum_up] += 1

        # 計算最多的裂縫
        max_crack = 0
        for key in crack.keys():
            max_crack = max(max_crack, crack[key])
        
        return height - max_crack
