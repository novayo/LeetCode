class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        
        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()
            
            if x != y:
                stones.insert(bisect.bisect_left(stones, y-x), y-x)

        if not stones:
            return 0
        else:
            return stones[0]
