class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        freq_buckets = ['' for _ in range(n+1)]
        
        counter = collections.Counter(s)
        
        for _s, freq in counter.items():
            freq_buckets[freq] += _s * freq
        
        ans = ''
        for string in freq_buckets[::-1]:
            ans += string
        return ans
        