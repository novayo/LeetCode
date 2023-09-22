class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)

        red, blue, green = costs[0]

        for i in range(1, n):
            new_red = min(blue, green) + costs[i][0]
            new_blue = min(red, green) + costs[i][1]
            new_green = min(red, blue) + costs[i][2]

            red, blue, green = new_red, new_blue, new_green

        return min(red, blue, green)
