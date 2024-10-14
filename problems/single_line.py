from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope = self.calcSlope(coordinates[0], coordinates[1])
        for i in range(2, len(coordinates)):
            if self.calcSlope(coordinates[0], coordinates[i]) != slope:
                return False
        return True

    def calcSlope(self, coord1, coord2):
        x1, y1 = coord1
        x2, y2 = coord2
        return (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else float('inf')