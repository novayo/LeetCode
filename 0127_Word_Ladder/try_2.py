class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        O(cnm) time / O(nm) space
        - where n is the length of wordList and m is the maximum length of strings in wordList c is the max length of items in Categorize table
        '''
        # Categorize
        table = collections.defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                target = word[:i] + '#' + word[i+1:]
                table[target].add(word)
        
        # init
        que = collections.deque()
        cache = set()
        que.append((beginWord, 1))
        cache.add(beginWord)
        
        # bfs
        while que:
            word, layer = que.popleft()
            
            if word == endWord:
                return layer
            
            for i in range(len(word)):
                target = word[:i] + '#' + word[i+1:]
                for next in table[target]:
                    if next in cache:
                        continue
                    que.append((next, layer + 1))
                    cache.add(next)
                del table[target]
        return 0