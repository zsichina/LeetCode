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
                if direction == 0:
                    row -= 1
                elif direction == 1:
                    col -= 1
                elif direction == 2:
                    row += 1
                elif direction == 3:
                    col += 1

                if (row, col) not in cleaned and robot.move():
                    backtrack(row, col, direction)

                if direction == 0:
                    row += 1
                elif direction == 1:
                    col += 1
                elif direction == 2:
                    row -= 1
                elif direction == 3:
                    col -= 1

                direction = (direction + 1)%4
                if i == 3:
                    robot.turnRight()
                    robot.move()
                    robot.turnLeft()
                    robot.turnLeft()
                else:
                    robot.turnLeft()

        cleaned = set()
        backtrack(0, 0, 0)
