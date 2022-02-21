class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def backtracking(start_index, cur_list):
            if len(cur_list) == k:
                ans.append(cur_list.copy())
                return
            if start_index >= n+1:
                return
            
            for i in range(start_index, n+1):
                cur_list.append(i)
                backtracking(i+1, cur_list)
                cur_list.pop()
        
        backtracking(1, [])
        return ans