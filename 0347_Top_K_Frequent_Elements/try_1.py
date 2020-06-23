class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = collections.defaultdict(int)
        
        for n in nums:
            table[n] += 1
        
        return [i for i, j in sorted(table.items(), key=lambda x: x[1], reverse=True)[:k]]
