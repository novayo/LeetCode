class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        stack = []
        index = 0

        while index < n:
            right_wall = height[index]

            if not stack or stack[-1][1] > right_wall:
                stack.append((index, right_wall))
                index += 1
            else:
                middle_idx, middle_val = stack.pop()

                if not stack:
                    continue

                left_wall_idx = stack[-1][0]
                left_wall = height[left_wall_idx]

                _height = min(left_wall, right_wall) - middle_val
                _width = index - left_wall_idx - 1
                ans += _height * _width
        return ans

