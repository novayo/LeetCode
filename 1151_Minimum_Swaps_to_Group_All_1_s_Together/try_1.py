class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n = len(data)
        totalOnes = sum(data)
        maxOnes = sum(data[:totalOnes])
        ans = maxOnes
        i, j = 0, totalOnes-1
        while j < n:
            i, j = i+1, j+1
            if j >= n:
                break
            maxOnes += -data[i-1] + data[j]
            ans = max(ans, maxOnes)
        return totalOnes - ans
