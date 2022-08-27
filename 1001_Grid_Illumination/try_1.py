class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        # init
        lamps_counter = collections.Counter()
        rows_counter = collections.Counter()
        cols_counter = collections.Counter()
        diag_counter = collections.Counter()
        anti_diag_counter = collections.Counter()
        
        for x, y in lamps:
            rows_counter[x] += 1
            cols_counter[y] += 1
            diag_counter[x-y] += 1
            anti_diag_counter[x+y] += 1
            lamps_counter[x, y] += 1
        
        # loop answer
        ans = []
        for x, y in queries:
            # check is shining or not
            if rows_counter[x] or cols_counter[y] or diag_counter[x-y] or anti_diag_counter[x+y]:
                ans.append(1)
            else:
                ans.append(0)
            
            # loop 8 adjacent cells
            for x_d in [-1, 0, 1]:
                for y_d in [-1, 0, 1]:
                    i, j = x+x_d, y+y_d
                    
                    if not (0 <= i < n and 0 <= j < n) or lamps_counter[i, j] == 0:
                        continue

                    num = lamps_counter[i, j]
                    rows_counter[i] -= num
                    cols_counter[j] -= num
                    diag_counter[i-j] -= num
                    anti_diag_counter[i+j] -= num
                    lamps_counter[i, j] = 0

        return ans