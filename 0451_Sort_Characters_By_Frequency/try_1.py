class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        list = []
        for k, v in counter.items():
            list.append((v, k))
        
        list.sort(reverse=True)
        
        ans = ""
        for times, v in list:
            ans += v*times
        return ans
