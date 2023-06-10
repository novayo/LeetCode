class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        counter = collections.Counter()
        
        for num, start, end in trips:
            counter[start] += num
            counter[end] -= num
        
        cur = 0
        for time in sorted(counter.keys()):
            cur += counter[time]
            if cur > capacity:
                return False
        return True
        