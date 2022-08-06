class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        
        if n == 0 or n % 2 == 1:
            return []
        
        ans = []
        counter = collections.Counter()
        for v in sorted(changed):
            half = v//2
            
            if half not in counter or v % 2 == 1:
                counter[v] += 1
                continue
            
            counter[half] -= 1
            if counter[half] == 0:
                del counter[half]
            ans.append(half)
        
        return ans if len(counter) == 0 else []