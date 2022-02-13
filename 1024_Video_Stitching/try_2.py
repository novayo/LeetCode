class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        '''
        greedy => 每次都挑最遠的就好
        '''
        n = len(clips)
        i = cur_end = ans = 0
        clips.sort()
        
        while cur_end < time:
            ans += 1
            
            next_end = 0
            while i < n and clips[i][0] <= cur_end:
                next_end = max(next_end, clips[i][1])
                i += 1
            
            if cur_end == next_end:
                return -1
            else:
                cur_end = next_end
        
        return ans