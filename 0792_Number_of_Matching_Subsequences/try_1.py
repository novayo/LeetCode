class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        counter = collections.Counter(words)
        
        queue = set()
        queue.add(s)
        
        ans = 0
        while queue:
            string = queue.pop()
            
            for i in range(len(string)):
                target = string[:i] + string[i+1:]
                
                if target in counter:
                    ans += counter.get(target)
                    del counter[target]
                
                queue.add(target)
        
        return ans
