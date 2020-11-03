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
        
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3
        
        def moveBack():
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
        
        def backtrack(i, j, direction, visited):
            # 如果不能走就不走
            # 如果走過了就不走
            # 若四個方向都走過了就backtrack，回到上一個狀態(方向)
            
            robot.clean()
            visited.add((i, j))
            
            for d in range(4):
                next_direction = (direction + d) % 4
                
                if next_direction == UP and (i-1, j) not in visited:
                    if robot.move():
                        backtrack(i-1, j, next_direction, visited)
                        moveBack()
                elif next_direction == RIGHT and (i, j+1) not in visited:
                    if robot.move():
                        backtrack(i, j+1, next_direction, visited)
                        moveBack()
                elif next_direction == DOWN and (i+1, j) not in visited:
                    if robot.move():
                        backtrack(i+1, j, next_direction, visited)
                        moveBack()
                elif next_direction == LEFT and (i, j-1) not in visited:
                    if robot.move():
                        backtrack(i, j-1, next_direction, visited)
                        moveBack()
                robot.turnLeft()
        
        
        backtrack(0, 0, UP, set())