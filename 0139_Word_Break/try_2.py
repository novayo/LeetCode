class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def BFS(firstIndex, maxlen):
            dp = [0] * len(s)
            indexQueue = collections.deque()
            indexQueue.append(firstIndex)
            
            while indexQueue:
                index = indexQueue.popleft()
                if dp[index] == 0:
                    for i in range(1, maxlen + 1):
                        if s[index: index+i] in wordDict:
                            if index+i == len(s): return True
                            indexQueue.append(index+i)
                            dp[index] = 1
            return False
                
        # get max len
        maxlen = 0
        for i in wordDict:
            maxlen = max(maxlen, len(i))
        
        return BFS(0, maxlen)
