class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def recr(cur_list, index):
            nonlocal ans
            
            if len(cur_list) == k:
                ans.append(cur_list[:])
                return
            
            for i in range(index, n+1):
                if len(cur_list) + n - i + 1 < k:
                    return
                recr(cur_list + [i], i+1)
        
        ans = []
        recr([], 1)
        return ans