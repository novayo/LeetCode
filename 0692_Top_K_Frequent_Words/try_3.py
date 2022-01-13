class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        counter = collections.Counter(words)
        
        # bucket sort
        buckets = collections.defaultdict(list)
        for string, count in counter.items():
            buckets[count].append(string)
        
        ans = []
        for count in sorted(buckets.keys(), reverse=True):
            ans += sorted(buckets[count])
            if len(ans) >= k:
                break
        
        return ans[:k]
