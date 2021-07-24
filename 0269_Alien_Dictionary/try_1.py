class Solution:
    def alienOrder(self, words: List[str]) -> str:
        after = {}
        
        for word in words:
            for a in word:
                after[a] = []
        
        for first, second in zip(words, words[1:]):
            for a, b in zip(first, second):
                if a != b:
                    after[b].append(a)
                    break
            else:
                if len(second) < len(first):
                    return ""
        
        seen = {}
        output = []
        
        def recr(node):
            nonlocal output
            if node in seen:
                return seen[node]
            
            seen[node] = False
            for next in after[node]:
                if not recr(next):
                    return False
            
            seen[node] = True
            output.append(node)
            return True
        
        for node in after:
            if not recr(node):
                return ''
        return ''.join(output)
