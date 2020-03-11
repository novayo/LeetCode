class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 0
        table = {}
        
        for i in range(len(points)):
            duplicate = 1
            for j in range(i+1, len(points)):
                if points[i] == points[j]:
                    duplicate += 1
                    continue
                
                tmp = 0
                for k in range(len(points)):
                    if (table.get((i,j,k)) or table.get((i,k,j)) or table.get((j,i,k)) or\
                        table.get((j,k,i)) or table.get((k,i,j)) or table.get((k,j,i))):
                        continue
                    table[k, i, j] = True
                    if (points[i][1]-points[j][1])*(points[i][0]-points[k][0]) ==\
                       (points[i][1]-points[k][1])*(points[i][0]-points[j][0]):
                        tmp += 1
                ans = max(ans, tmp)
            ans = max(ans, duplicate)
        
        return ans
