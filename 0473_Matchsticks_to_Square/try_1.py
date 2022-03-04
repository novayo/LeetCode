class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        
        if s % 4 != 0:
            return False
        
        target = s // 4
        num_bucket = 4
        
        matchsticks.sort()
        if matchsticks[-1] > target:
            return False
        
        while matchsticks and matchsticks[-1] == target:
            matchsticks.pop()
            num_bucket -= 1
        
        n = len(matchsticks)
        def recr(buckets, index):
            if index < 0:
                return True
            
            for i in range(num_bucket):
                buckets[i] += matchsticks[index]
                if buckets[i] <= target:
                    if recr(buckets, index-1):
                        return True
                buckets[i] -= matchsticks[index]
                if buckets[i] == 0:
                    break
            return False
        
        return recr([0] * num_bucket, n-1)
