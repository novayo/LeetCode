class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        def isSame(s1, s2, mask):
            if s1 == s2:
                return True
            if (s1, s2) in memo or (s2, s1) in memo:
                return True
            
            mask.add(s1)
            
            for neighbor in graph[s1]:
                if neighbor in mask:
                    continue
                
                if isSame(neighbor, s2, mask):
                    mask.remove(s1)
                    memo.add((neighbor, s2)) # 不用memo false的情況，因為整個函數直接return False了
                    memo.add((neighbor, s1))
                    return True
            
            mask.remove(s1)
            return False
        
        
        # boundary check
        if len(sentence1) != len(sentence2):
            return False
            
        # 先初始化雙向圖
        graph = collections.defaultdict(set)
        for s1, s2 in similarPairs:
            graph[s1].add(s2)
            graph[s2].add(s1)
        
        # DFS Check answer
        memo = set()
        for s1, s2 in zip(sentence1, sentence2):
            if isSame(s1, s2, set()) == False:
                return False
            memo.add((s1, s2))
        
        return True