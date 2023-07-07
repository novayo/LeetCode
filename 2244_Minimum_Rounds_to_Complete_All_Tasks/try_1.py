class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = collections.Counter()
        for task in tasks:
            counter[task] += 1
        
        ans = 0
        for task, count in counter.items():
            if count == 1:
                return -1
            
            ans += count // 3 + (count % 3 > 0)
        
        return ans
        
