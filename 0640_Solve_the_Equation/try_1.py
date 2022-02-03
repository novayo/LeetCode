class Solution:
    def solveEquation(self, equation: str) -> str:
        def build_info(part, part_info):
            constant = ''
            for_x = False
            for s in part[::-1]:
                if s == 'x':
                    for_x = True
                elif s.isdigit():
                    constant = s + constant
                else:
                    # + -
                    if constant == '': constant='1'
                    num = int(s+constant)
                    if for_x:
                        part_info[0] += num
                    else:
                        part_info[1] += num

                    constant = ''
                    for_x = False
            if constant or for_x:
                if constant == '': constant = '1'
                if for_x:
                    part_info[0] += int(constant)
                else:
                    part_info[1] += int(constant)
        
        
        left_part, right_part = equation.split('=')
        left_part_info = [0, 0]  # ax+b
        right_part_info = [0, 0] # ax+b
        build_info(left_part, left_part_info)
        build_info(right_part, right_part_info)
        
        x_constant = left_part_info[0] - right_part_info[0]
        x_value = right_part_info[1] - left_part_info[1]
        
        if x_constant == 0 and x_value == 0:
            return 'Infinite solutions'
        elif x_constant == 0 and x_value != 0:
            return 'No solution'
        
        x_value = x_value // x_constant
        
        return f'x={x_value}'
            
