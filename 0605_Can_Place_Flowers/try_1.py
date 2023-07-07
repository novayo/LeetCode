class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 能種就直接種
        length = len(flowerbed)
        
        for i, v in enumerate(flowerbed):
            if n == 0:
                break

            if v == 1:
                continue
            
            # 檢查是否能種
            if (i == 0 or flowerbed[i-1] == 0) and (i == length-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
            
        return n == 0
            
