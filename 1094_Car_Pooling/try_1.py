class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        table = collections.defaultdict(int)
        
        for num, start, end in trips:
            table[start] += num
            table[end] -= num
        
        cur_capacity = 0
        for time in sorted(table.keys()):
            cur_capacity += table[time]
            
            if cur_capacity > capacity:
                return False
        return True