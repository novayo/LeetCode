class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old_color = image[sr][sc]
        
        if old_color == newColor:
            return image
        
        
        width = len(image[0])
        height = len(image)
        
        
        queue = collections.deque()
        queue.appendleft((sr, sc))
        found = set()
        found.add((sr, sc))
        while queue:
            x, y = queue.pop()
            
            image[x][y] = newColor
            
            for i, j in [x, y-1], [x, y+1], [x-1, y], [x+1, y]:
                if i < 0 or j < 0 or i >= height or j >= width or (i, j) in found:
                    continue
                
                if image[i][j] == old_color:
                    found.add((i, j))
                    queue.appendleft((i, j))
        
        return image