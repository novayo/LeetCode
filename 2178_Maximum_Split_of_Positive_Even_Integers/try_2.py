class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        '''
        2: [2]
        4: [4]
        6: [2+4]
        8: [2+6]
        10: [2+8]
        12: [2+4+6]
        14: [2+4+8]
        16: [2+4+6+4]
        18: [2+4+12]
        
        [2+4+6+8] = 20
        '''
        if finalSum % 2 == 1:
            return []
        
        ans = []
        cur_sum = 0
        for i in range(1, finalSum+1):
            if cur_sum + i*2 <= finalSum:
                ans.append(i*2)
                cur_sum += i*2
            else:
                break
        
        remain = finalSum - cur_sum
        if remain > 0:
            if remain <= ans[-1]:
                ans[-1] += remain
            else:
                ans.append(remain)
        return ans
