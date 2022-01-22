class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        def calculate(rows, cols):
            ret = 0
            i1 = i2 = 0
            while i1 < len(rows) and i2 < len(cols):
                if rows[i1][0] == cols[i2][0]:
                    ret += rows[i1][1] * cols[i2][1]
                    i1, i2 = i1+1, i2+1
                elif rows[i1][0] < cols[i2][0]:
                    i1 += 1
                else:
                    i2 += 1
            return ret
        
        table1 = collections.defaultdict(list)
        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                if mat1[i][j] != 0:
                    table1[i].append((j, mat1[i][j]))
        
        table2 = collections.defaultdict(list)
        for i in range(len(mat2)):
            for j in range(len(mat2[0])):
                if mat2[i][j] != 0:
                    table2[j].append((i, mat2[i][j]))
        
        ans = [[0] * len(mat2[0]) for _ in range(len(mat1))]
        for i in range(len(ans)):
            for j in range(len(ans[0])):
                ans[i][j] = calculate(table1.get(i, []), table2.get(j, []))
        
        return ans
