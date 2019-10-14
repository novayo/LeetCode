class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        query = collections.deque()
        for v in queries:
            query.append(min(collections.Counter(v).items())[1])
        word = collections.deque()
        for v in words:
            word.append(min(collections.Counter(v).items())[1])
        ans = collections.deque()
        for v in query:
            _ = 0
            for k in word:
                if k > v:
                    _ += 1
            ans.append(_)
        return ans
