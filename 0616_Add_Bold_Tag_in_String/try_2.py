class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        '''
        transform to LC56
        '''
        def add_into_interval(start, end):
            i = bisect.bisect_left(bold_range, start)
            j = bisect.bisect_right(bold_range, end)
            
            if i%2 == 0 and j%2 == 0:
                bold_range[i:j] = [start, end]
            elif i%2 == 0 and j%2 == 1:
                bold_range[i:j] = [start]
            elif i%2 == 1 and j%2 == 0:
                bold_range[i:j] = [end]
            else:
                bold_range[i:j] = []
        
        
        bold_range = []
        for word in words:
            for i in range(len(s)-len(word)+1):
                if s[i: i+len(word)] == word:
                    add_into_interval(i, i+len(word))
        
        
        ans = ''
        cur_index = 0
        for i in range(len(bold_range)//2):
            start = bold_range[i*2]
            end = bold_range[i*2+1]
            
            if cur_index < start:
                ans += s[cur_index: start]
            
            ans += '<b>' + s[start: end] + '</b>'
            cur_index = end
        
        if cur_index < len(s):
            ans += s[cur_index:]
        return ans
        