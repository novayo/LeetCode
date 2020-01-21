# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        pos = set()
        
        def dfs(x, y, face=0):
            pos.add((x,y))
            robot.clean()
            for k in range(4):
                tmp_x, tmp_y = x, y
                if face == 0: tmp_y -= 1
                elif face == 1: tmp_x += 1
                elif face == 2: tmp_y += 1
                else: tmp_x -= 1        
                
                if (tmp_x, tmp_y) not in pos and robot.move():
                    dfs(tmp_x , tmp_y, face)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                
                robot.turnRight()
                face = (face + 1)%4
        
        dfs(0, 0)
