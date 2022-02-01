class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        category = collections.defaultdict(set)
        for x, y in points:
            category[y].add(x)
        
        ans_x = set()
        
        for y, x_set in category.items():
            x_list = sorted(list(x_set))
            
            l, r = 0, len(x_list)-1
            while l <= r:
                ans_x.add((x_list[l]+x_list[r]) / 2)
                if len(ans_x) >= 2:
                    return False
                l, r = l+1, r-1
        
        return True
            
