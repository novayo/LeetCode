class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        height, width = len(picture), len(picture[0])
        rows = collections.defaultdict(int)
        cols = collections.defaultdict(int)
        
        for i in range(height):
            for j in range(width):
                if picture[i][j] == 'B':
                    rows[i] += 1
                    cols[j] += 1
        
        ans = 0
        for i in range(height):
            for j in range(width):
                if picture[i][j] == 'B' and rows[i] == 1 and cols[j] == 1:
                    ans += 1
        return ans
