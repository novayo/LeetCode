class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        height = len(wall)
        table = collections.Counter()

        for i in range(height):
            presum = 0
            for j in range(len(wall[i])-1):
                presum += wall[i][j]
                table[presum] += 1
                
        if len(table) == 0:
            return height
        else:
            return height - max(table.values())