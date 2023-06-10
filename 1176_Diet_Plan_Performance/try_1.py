class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        ans = 0

        curSum = sum(calories[:k])
        if curSum < lower:
            ans -= 1
        elif curSum > upper:
            ans += 1

        i = 0
        for j in range(k, len(calories)):
            curSum += -calories[i] + calories[j]

            if curSum < lower:
                ans -= 1
            elif curSum > upper:
                ans += 1

            i += 1
        return ans