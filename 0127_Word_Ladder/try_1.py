class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # bfs
        wordDict = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                wordDict[word[:i] + "*" + word[i+1:]].append(word)
        
        queue = collections.deque()
        queue.append((beginWord, 1))
        
        wordset = set()
        while queue:
            target, times = queue.popleft()
            
            for i in range(len(target)):
                tmp = target[:i] + "*" + target[i+1:]
                if tmp in wordDict:
                    for found in wordDict[tmp]:
                        if found in wordset:
                            continue
                        else:
                            wordset.add(found)
                        if found == endWord:
                            return times+1
                        else:
                            queue.append((found, times+1))
        return 0
