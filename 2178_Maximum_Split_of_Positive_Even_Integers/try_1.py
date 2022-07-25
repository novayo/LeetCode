class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        # O(10**5) time / O(10**5) space
        if finalSum % 2 == 1:
            return []
        
        cur_sum = 0
        i = 2
        ans = []
        while cur_sum + i <= finalSum:
            ans.append(i)
            cur_sum += i
            i += 2
        
        cur_sum -= ans.pop()
        ans.append(finalSum-cur_sum)
        return ans
