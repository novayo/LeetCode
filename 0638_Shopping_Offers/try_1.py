class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        
        memo = {}
        def recr(needs):
            if all([need == 0 for need in needs]):
                return 0
            
            key = tuple(needs)
            if key not in memo:
                # don't choose
                ret = 0
                for i in range(len(needs)):
                    ret += price[i] * needs[i]

                # if choose
                for s in special:

                    if any([needs[i] - s[i] < 0 for i in range(len(needs))]):
                        continue
                    
                    for i in range(len(needs)):
                        needs[i] -= s[i]

                    ret = min(ret, s[-1] + recr(needs))

                    for i in range(len(needs)):
                        needs[i] += s[i]

                memo[key] = ret
            return memo[key]
        
        return recr(needs)