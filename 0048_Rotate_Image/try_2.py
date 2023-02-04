class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        left_top = [0, 0]
        right_top = [0, n-1]
        left_down = [n-1, 0]
        right_down = [n-1, n-1]
        
        for level in range(n//2):
            for step in range(n-1-2*level):
                matrix[left_top[0]+level][left_top[1]+level+step], \
                matrix[right_top[0]+level+step][right_top[1]-level], \
                matrix[right_down[0]-level][right_down[1]-level-step], \
                matrix[left_down[0]-level-step][left_down[1]+level] = \
                    matrix[left_down[0]-level-step][left_down[1]+level], \
                    matrix[left_top[0]+level][left_top[1]+level+step], \
                    matrix[right_top[0]+level+step][right_top[1]-level], \
                    matrix[right_down[0]-level][right_down[1]-level-step]

