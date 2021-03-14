class Solution:
    def trap(self, height: List[int]) -> int:
        # 取得第一個值
        endPos = len(height)
        i = 0
        while i < endPos:
            if height[i] != 0:
                break
            i+=1
        
        # 移動 (Monotonic Stack)
        ans = 0
        startPos = i # 起點位置
        move = i + 1 # 移動位置
        while move < endPos:
            # 結算
            if (height[startPos] <= height[move]):
                traceBack = move - 1
                while startPos < traceBack:
                    ans += height[startPos] - height[traceBack]
                    traceBack -= 1
                
                startPos = move
            move += 1
        
        # 剩下最後一組 
        #   現在的 一定是startPos為最大值，move為len(height)
        # 所以反過來再做一次
        
        # 取得第一個值
        endPos = startPos - 1 # 定義新的終點位置
        i = move - 1
        while i > endPos + 1:
            if height[i-1] < height[i]:
                break
            i-=1
        
        startPos = i # 起點位置
        move = i - 1 # 移動位置
        while endPos < move :
            # 結算
            if (height[startPos] <= height[move]):
                traceBack = move + 1
                while startPos > traceBack:
                    ans += height[startPos] - height[traceBack]
                    traceBack += 1
                startPos = move
            move -= 1
        
        return ans
