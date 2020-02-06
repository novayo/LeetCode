class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        first = second = -1
        lastFruitNum = 0
        ans = -float('inf')
        tmp_ans = 0
        
        for t in tree:
            # 紀錄數量
            if t == first or t == second:
                tmp_ans += 1
            else:
                tmp_ans = lastFruitNum + 1 # 舊的 + 一個新的
            
            # 遇到舊的
            if t == first:
                lastFruitNum += 1
            else:
                lastFruitNum = 1 # 新的水果（也算一個）
            
            # 如果遇到新的，要讓first變成新的（跟second交換）
            if t != first:
                second, first = first, t
            
            # 更新答案
            ans = max(ans, tmp_ans)
        
        return ans
