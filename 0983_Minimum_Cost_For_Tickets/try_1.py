class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        memo = {}
        def recr(index):
            if index >= len(days):
                return 0
            
            start_day = days[index]
            index_of_one_day = bisect.bisect_left(days, start_day + 1)
            index_of_seven_day = bisect.bisect_left(days, start_day + 7)
            index_of_thirty_day = bisect.bisect_left(days, start_day + 30)
            
            if index not in memo:
                memo[index] = min(
                    costs[0] + recr(index_of_one_day),
                    costs[1] + recr(index_of_seven_day),
                    costs[2] + recr(index_of_thirty_day),
                )
            return memo[index]
        
        return recr(0)
