class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        for i, w in enumerate(words):
            words[i] = w.count(min(w))
        words.sort()
        
        ans = collections.deque()
        for query in queries:
            q = query.count(min(query))
            ans.append(len(words) - bisect.bisect_right(words, q, 0, len(words)))
        
        return ans
