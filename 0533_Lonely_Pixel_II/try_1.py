class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        height = len(picture)
        width = len(picture[0])
        
        row_string_map = [''.join(p) for p in picture]
        
        row_map = collections.Counter()
        col_map = collections.Counter()
        for i in range(height):
            for j in range(width):
                if picture[i][j] == 'B':
                    col_map[j] += 1
                    row_map[i] += 1
        
        for i in range(height):
            for j in range(width):
                if picture[i][j] == 'B' and col_map[j] == target and row_map[i] == target:
                    picture[i][j] = 'X'
        
        ans = 0
        for j in range(width):
            all_x = 0
            same = ''
            for i in range(height):
                if picture[i][j] == 'B':
                    all_x = 0
                    break
                elif picture[i][j] == 'X':
                    if not same:
                        same = row_string_map[i]
                    elif same != row_string_map[i]:
                        all_x = 0
                        break
                    all_x += 1
            ans += all_x
        
        return ans
                