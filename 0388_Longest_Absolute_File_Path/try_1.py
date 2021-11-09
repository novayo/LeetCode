class Solution:
    def lengthLongestPath(self, input: str) -> int:
        def get(string):
            count = 0
            
            i = 0
            while i < len(string):
                if string[i] == '\t':
                    count += 1
                    i += 1
                else:
                    break
            
            return count, string[i:]
        
        ans = 0
        cur_string = []
        for v in input.split('\n'):
            cur_level = len(cur_string)-1
            level, ele = get(v)
            
            if level == cur_level:
                cur_string[-1] = ele
            elif level > cur_level:
                cur_string.append(ele)
            else:
                while len(cur_string)-1 > level:
                    cur_string.pop()
                cur_string[-1] = ele
            
            if '.' in ele:
                ans = max(ans, len('/'.join(cur_string)))
        
        return ans
            