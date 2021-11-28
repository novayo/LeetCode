class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
        bucket sort => 用frequency 當作桶子，再依照freq排序，最後取出前幾個即可
        '''
        
        buckets = [[] for _ in range(len(words)+1)]
        counter = collections.Counter(words)
        
        for word, freq in counter.items():
            buckets[freq].extend([word])
        
        ans = []
        for bucket in buckets[::-1]:
            if len(ans) < k:
                ans.extend(sorted(bucket))
            else:
                break
        
        return ans[:k]
