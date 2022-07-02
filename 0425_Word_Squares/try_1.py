class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        
        def gen_candidate(word, idx, candidates):
            ret = []
            for i in range(idx+1, len(word)):
                tmp = []
                for candidate in candidates:
                    if word[i] == candidate[idx]:
                        tmp.append(candidate)
                if not tmp:
                    return []
                ret.append(tmp)
            return ret
        
        def my_filter(word, idx, candidates):
            ret = []
            for i in range(len(candidates)):
                tmp = []
                for candidate in candidates[i]:
                    if candidate[idx] == word[i+idx+1]:
                        tmp.append(candidate)
                
                if not tmp:
                    return []
                
                ret.append(tmp)
            return ret
                
        def recr(candidates, layer, t_length):
            if len(candidates) == 1:
                return [[val] for val in candidates[0]]
            
            ret = []
            for word in candidates[0]:
                remain = my_filter(word, layer, candidates[1:])
                if not remain:
                    continue
                    
                for next in recr(remain, layer+1, t_length):
                    ret.append([word] + next)
            return ret
        
        
        length_dict = collections.defaultdict(list)
        for word in words:
            length_dict[len(word)].append(word)
            
        
        ans = []
        for length in range(1, 5):
            for word in length_dict[length]:
                if length == 1:
                    ans.append([word])
                    continue
                
                remain = gen_candidate(word, 0, words)
                
                if not remain:
                    continue
                  
                for next in recr(remain, 1, length):
                    ans.append([word] + next)
                    
        return ans
