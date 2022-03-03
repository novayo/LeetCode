class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        
        memo = {}
        def recr(start, cur_list):
            nonlocal ans
            
            if start >= len(s):
                ans.append(cur_list[:])
                return
            
            for end in range(start, len(s)):
                if s[start] == s[end] and (end-start <= 2 or (start+1, end-1) in memo):
                    memo[start, end] = True
                    recr(end+1, cur_list + [s[start: end+1]])
        
        recr(0, [])
        return ans
        