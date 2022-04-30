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
        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
        
        def moveBack():
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
        
        
        cache = set()
        cache.add((0, 0))
        def recr(i, j, face):
            
            robot.clean()
            
            for _ in range(4):
                face = (face+1) % 4
                robot.turnRight()
                
                if face == UP:
                    x, y = i-1, j
                elif face == RIGHT:
                    x, y = i, j+1
                elif face == DOWN:
                    x, y = i+1, j
                else:
                    x, y = i, j-1
                
                if (x, y) not in cache:
                    cache.add((x, y))
                    if robot.move():
                        recr(x, y, face)
                        moveBack()
        
        recr(0, 0, UP)
