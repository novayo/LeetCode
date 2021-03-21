class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        
        dp = [0] * (len(courses) + 1)
        cur_index = 0
        for t, d in courses:
            j = cur_index - 1
            if dp[cur_index] + t <= d:
                cur_index += 1
                dp[cur_index] = dp[cur_index-1] + t
            
            while j >= 0:
                dp[j+1] = min(dp[j+1], dp[j]+t)
                j -= 1
        
        return cur_index
