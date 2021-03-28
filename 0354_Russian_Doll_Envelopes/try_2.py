class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # patient sort
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        tails = []
        for e in envelopes:
            left = 0
            right = len(tails)
            while left != right:
                mid = left + (right - left) // 2
                if tails[mid][1] < e[1]:
                    left = mid + 1
                else:
                    right = mid
                
            index = left
            if index == len(tails):
                tails.append(e)
            else:
                tails[index] = e
        
        return len(tails)