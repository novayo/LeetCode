class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(i, j, target):
            if i<0 or j<0 or i>=len(image) or j>=len(image[0]) or image[i][j] != target:
                return
            image[i][j] = 'x'
            dfs(i-1,j, target)
            dfs(i,j+1, target)
            dfs(i+1,j, target)
            dfs(i,j-1, target)
        
        dfs(sr, sc, image[sr][sc])
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == 'x':
                    image[i][j] = newColor
        return image
