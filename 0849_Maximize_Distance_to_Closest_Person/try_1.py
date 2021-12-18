class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # find first seated
        i = 0
        while i < len(seats):
            if seats[i] == 1:
                break
            i += 1
        
        # find end seated
        j = 0
        while j >= 0:
            if seats[len(seats) - j - 1] == 1:
                break
            j += 1
        
        ans = max(i, j)
        
        # loop
        for j in range(i+1, len(seats)-j):
            if seats[j] == 1:
                ans = max(ans, (j-i) // 2)
                i = j
        
        return ans
