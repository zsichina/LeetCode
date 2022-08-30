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
        def backtrack(row, col, direction):
            robot.clean()
            cleaned.add((row, col))

            for i in range(4):
                r, c = directions[direction]
                if (row + r, col + c) not in cleaned and robot.move():
                    backtrack(row + r, col + c, direction)

                direction = (direction + 1)%4
                if i == 3:
                    robot.turnRight()
                    robot.move()
                    robot.turnLeft()
                    robot.turnLeft()
                else:
                    robot.turnLeft()

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        cleaned = set()
        backtrack(0, 0, 0)
