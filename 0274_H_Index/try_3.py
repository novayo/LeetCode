class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        
        for i, v in enumerate(citations):
            if i >= v:
                return i
        return len(citations)