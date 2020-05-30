class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        table = collections.defaultdict(list)
        smallest_length = float('inf')
        for x, y in points:
            length = x**2+y**2
            smallest_length = min(smallest_length, length)
            table[length].append([x,y])
        
        ans = []
        for k in sorted(table.keys()):
            if K <= 0:
                break
            for v in table[k]:
                ans.append(v)
            K -= len(table[k])
        
        if K == 0:
            return ans
        else:
            # K<0
            while K<0:
                ans[-1].pop()
                K += 1
            return ans
