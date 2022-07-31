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
        cache = set()
        
        def rollback():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def recr(x, y, face):
            cache.add((x, y))
            robot.clean()
            
            for i in range(4):
                face = (face+1) % 4
                robot.turnRight()
                
                if face == UP and (x-1, y) not in cache and robot.move():
                    recr(x-1, y, face)
                    rollback()
                elif face == RIGHT and (x, y+1) not in cache and robot.move():
                    recr(x, y+1, face)
                    rollback()
                elif face == DOWN and (x+1, y) not in cache and robot.move():
                    recr(x+1, y, face)
                    rollback()
                elif face == LEFT and (x, y-1) not in cache and robot.move():
                    recr(x, y-1, face)
                    rollback()
        
        recr(0, 0, UP)
        