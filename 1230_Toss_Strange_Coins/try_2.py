class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        
        def recr(index):
            if index >= len(prob):
                return {0: 1}
            
            ret = collections.defaultdict(int)
            for cur_target, cur_prob in recr(index+1).copy().items():
                ret[cur_target] += cur_prob * (1-prob[index])
                if cur_target + 1 <= target:
                    ret[cur_target + 1] += cur_prob * prob[index]
            return ret
        
        return recr(0)[target]
