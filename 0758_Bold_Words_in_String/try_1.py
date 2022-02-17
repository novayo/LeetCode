class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        def add_to_interval(start, end):
            i = bisect.bisect_left(bold_intervals, start)
            j = bisect.bisect_right(bold_intervals, end)
            
            if i%2 == 0 and j%2 == 0:
                bold_intervals[i:j] = [start, end]
            elif i%2 == 0 and j%2 == 1:
                bold_intervals[i:j] = [start]
            elif i%2 == 1 and j%2 == 0:
                bold_intervals[i:j] = [end]
            else:
                bold_intervals[i:j] = []
        
        
        bold_intervals = []
        for word in words:
            n = len(word)
            for i in range(len(s)-n+1):
                if s[i: i+n] == word:
                    add_to_interval(i, i+n)
        
        
        ans = ''
        cur_index = 0
        for i in range(len(bold_intervals) // 2):
            start = bold_intervals[i*2]
            end = bold_intervals[i*2+1]
            
            if cur_index < start:
                ans += s[cur_index: start]
            
            ans += '<b>' + s[start: end] + '</b>'
            cur_index = end
        
        if cur_index < len(s):
            ans += s[cur_index:]
        
        return ans