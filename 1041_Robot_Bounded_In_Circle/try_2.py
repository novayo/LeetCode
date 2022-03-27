class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0, 0]
        face = 0

        for retry in range(4):
            for d in instructions:
                # move
                if d == 'G':
                    if face == 0:
                        pos[0] -= 1
                    elif face == 1:
                        pos[1] += 1
                    elif face == 2:
                        pos[0] += 1
                    else:
                        pos[1] -= 1
                elif d == 'L':
                    face -= 1
                    if face < 0:
                        face = 3
                else:
                    face += 1
                    if face > 3:
                        face = 0

            # check if back to original
            if pos == [0, 0] and face == 0:
                return True
        
        return False
