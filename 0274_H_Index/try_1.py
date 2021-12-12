class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        H-Index：有i個至少為i，且剩下的均小於i => 回傳最大i
        '''
        # 且剩下的均小於i
        citations.sort(reverse=True)
        
        for i, c in enumerate(citations):
            # 有i個至少為i
            if i >= c:
                # 回傳最大i
                return i
        return len(citations)
        
