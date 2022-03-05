class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        
        def recr(cur_list, cur_sum, index, bitmask=0):
            nonlocal ans
            
            if cur_sum == n:
                if len(cur_list) == k:
                    ans.append(cur_list[:])
                return
            
            for i in range(index, 10):
                if bitmask & (1<<i) != 0:
                    continue
                cur_sum += i
                if cur_sum <= n:
                    recr(cur_list + [i], cur_sum, i+1, bitmask | (1<<i))
                cur_sum -= i
        
        recr([], 0, 1)
        return ans
