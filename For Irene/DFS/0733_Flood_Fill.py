class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        def dfs(i, j, original_color):
            
            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) or image[i][j] != original_color:
                return
            
            image[i][j] = newColor
            dfs(i-1, j, original_color)
            dfs(i, j-1, original_color)
            dfs(i+1, j, original_color)
            dfs(i, j+1, original_color)
        
        if image[sr][sc] == newColor:
            return image
        
        dfs(sr, sc, image[sr][sc])
        return image
