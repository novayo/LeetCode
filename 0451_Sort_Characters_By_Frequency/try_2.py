class Solution:
    def frequencySort(self, s: str) -> str:
        '''
        bucket sort => freq as bucket => create string by freq
        '''
        
        buckets = ['' for _ in range(len(s)+1)]
        counter = collections.Counter(s)
        
        for _s, freq in counter.items():
            buckets[freq] += _s*freq

        ans = ''
        for string in buckets[::-1]:
            ans += string
        return ans
