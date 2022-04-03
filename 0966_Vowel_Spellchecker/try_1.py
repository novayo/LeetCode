class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def normalize(word):
            ret = ''
            for w in word.lower():
                if w in 'aeiou':
                    ret += '@'
                else:
                    ret += w
            return ret
            
        
        normalized = collections.defaultdict(list)
        for word in wordlist:
            normalized[normalize(word)].append(word)
        
        lowered = collections.defaultdict(list)
        for word in wordlist:
            lowered[word.lower()].append(word)
        
        wordlist = set(wordlist)
        for i in range(len(queries)):
            if queries[i] in wordlist:
                continue
            
            if queries[i].lower() in lowered:
                queries[i] = lowered[queries[i].lower()][0]
            else:
                word = normalize(queries[i])
                queries[i] = normalized.get(word, [''])[0]
        
        return queries
