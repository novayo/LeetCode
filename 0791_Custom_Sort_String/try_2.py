class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # greedy
        counter = collections.Counter(s)
        ans = ''
        
        # get answer
        for char in order:
            if char in counter:
                ans += char * counter[char]
                del counter[char]
        
        for char, num in counter.items():
            ans += char * num
        
        return ans
