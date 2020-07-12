class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        '''
        [[0,5],[4,6],[6,7],[7,10]]
        排序過後，
        去看是否 [0,5],[4,6] => 下一個的左邊(4) 是否大於 上一個的右邊(5)
        '''
        
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True
