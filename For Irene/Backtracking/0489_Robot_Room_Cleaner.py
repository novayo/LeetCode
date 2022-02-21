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

UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        
        # without changing status => don't change direction
        def rollback():
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
        
        memo = set()
        def backtracking(i, j, face):
            # in every pos
            robot.clean()
            memo.add((i, j))
            
            for d in range(4):
                next = (face + d) % 4
                
                if next == UP and (i-1, j) not in memo:
                    if robot.move():
                        backtracking(i-1, j, next)
                        rollback()
                elif next == RIGHT and (i, j+1) not in memo:
                    if robot.move():
                        backtracking(i, j+1, next)
                        rollback()
                elif next == DOWN and (i+1, j) not in memo:
                    if robot.move():
                        backtracking(i+1, j, next)
                        rollback()
                elif next == LEFT and (i, j-1) not in memo:
                    if robot.move():
                        backtracking(i, j-1, next)
                        rollback()
                        
                robot.turnRight()

        
        backtracking(0, 0, UP)
        