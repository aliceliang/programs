class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        x_diff = coordinates[1][0] - coordinates[0][0]
        y_diff = coordinates[1][1] - coordinates[0][1]
        index = 2
        if x_diff == 0:
            while index < len(coordinates):
                if coordinates[index][0] != coordinates[0][0]:
                    return False
                else:
                    index += 1
                    continue
        else:
            slope = y_diff / float(x_diff)
            while index < len(coordinates):
                expected_y = (coordinates[index][0] - coordinates[0][0])*slope + coordinates[0][1]
                if expected_y != coordinates[index][1]:
                    return False
                else:
                    index += 1
                    continue
        return True