class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        '''
        bfs: brute force
        '''
        def get_candidate(target_string):
            ret = []
            for s in bank:
                count = 0
                for a, b in zip(s, target_string):
                    if a != b:
                        count += 1
                if count == 1:
                    ret.append(s)
            return ret
        
        cache = set()
        container = [start]
        ans = 0
        
        while container:
            next_container = []
            
            
            for target_string in container:
                if target_string == end:
                    return ans
                
                if target_string in cache:
                    continue
                cache.add(target_string)
                next_container.extend(get_candidate(target_string))
            
            container = next_container
            ans += 1
            
        return -1
        
        
        
# ACGT
# Input: start = "AAAAACCC", end = "AACCCCCC", bank = ["AAACACCC","AAACCCCC","AACCCCCC"]
# Output: 3
