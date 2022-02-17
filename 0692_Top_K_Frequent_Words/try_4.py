class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        n = len(words)
        freq_buckets = [[] for _ in range(n+1)]
        
        counter = collections.Counter(words)
        
        for word, freq in counter.items():
            freq_buckets[freq].append(word)
        
        ans = []
        for word_list in freq_buckets[::-1]:
            word_list.sort()
            ans.extend(word_list)
            
            if len(ans) > k:
                break
                
        return ans[:k]