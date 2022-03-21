class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        diff = sorted([(a+b, i) for i, (a, b) in enumerate(zip(aliceValues, bobValues))], reverse=True)
        
        a = b = 0
        for i in range(n):
            if i%2 == 0:
                a += aliceValues[diff[i][1]]
            else:
                b += bobValues[diff[i][1]]
        
        if a-b > 0:
            return 1
        elif a-b == 0:
            return 0
        else:
            return -1