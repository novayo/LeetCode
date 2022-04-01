class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        def get_presum(arr):
            ret = [0] * len(arr)
            cur = 0
            for i, v in enumerate(arr):
                cur += int(v)
                ret[i] = cur
            return ret

        n = len(boxes)
        presum = get_presum(boxes)
        suffix = get_presum(boxes[::-1])[::-1]
        presum_presum = get_presum(presum)
        suffix_suffix = get_presum(suffix[::-1])[::-1]
        
        ans = [0] * n
        for i in range(n):
            ans[i] += presum_presum[i-1] if i > 0 else 0
            ans[i] += suffix_suffix[i+1] if i+1 < n else 0
        return ans