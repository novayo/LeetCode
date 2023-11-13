class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(string):
            i, j = 0, len(string)-1
            while i < j:
                if string[i] != string[j]:
                    return False
                i, j = i+1, j-1
            return True
        
        @lru_cache(None)
        def recr(string):
            if not string:
                return [[]]
            if len(string) == 1:
                return [[string]]
            
            ans = []
            for i in range(1, len(string)+1):
                sub_string = string[:i]

                if not isPalindrome(sub_string):
                    continue

                for ret_list in recr(string[i:]): 
                    ans.append([sub_string] + ret_list)
            return ans
        
        return recr(s)
