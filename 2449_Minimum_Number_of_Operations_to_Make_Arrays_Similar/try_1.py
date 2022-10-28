class Solution:
    def makeSimilar(self, nums: List[int], targets: List[int]) -> int:
        nums.sort()
        targets.sort()
        
        oddT, evenT = [], []
        oddN, evenN = [], []
        
        for num, target in zip(nums, targets):
            if num % 2:
                oddN.append(num)
            else:
                evenN.append(num)
                
            if target % 2:
                oddT.append(target)
            else:
                evenT.append(target)     
        
        add = mus = 0
        def helper(nums, targets):
            nonlocal add, mus 
            ans = 0
            for num, target in zip(nums, targets):
                if num < target:
                    diff = (target - num) // 2
                    if add >= diff:
                        add -= diff
                    else:
                        diff -= add
                        add = 0
                        ans += diff
                        mus += diff
                else:
                    diff = (num - target) // 2
                    if mus >= diff:
                        mus -= diff
                    else:
                        diff -= mus
                        mus = 0
                        ans += diff
                        add += diff   
            return ans
        
        return helper(oddN, oddT) + helper(evenN, evenT)
