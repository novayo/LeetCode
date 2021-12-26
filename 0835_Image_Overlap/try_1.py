class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        '''
        跑所有可能
        '''
        ans = 0
        for relative_i2 in range(-len(img2)+1, len(img1)):
            for relative_j2 in range(-len(img2[0])+1, len(img1[0])):
                count = 0
                for i2 in range(len(img2)):
                    i1 = relative_i2 + i2
                    if i1 < 0 or i1 >= len(img1):
                        continue
                    for j2 in range(len(img2[0])):
                        j1 = relative_j2 + j2
                        
                        if j1 < 0 or j1 >= len(img1[0]):
                            continue
                        
                        count += img1[i1][j1] == 1 and img2[i2][j2] == 1
                
                ans = max(ans, count)
        
        return ans
