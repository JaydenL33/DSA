from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convertTime(timeStr: str) -> int:
            splitTime = timeStr.split(":")
            hour = int(splitTime[0])
            minute = int(splitTime[1])
            return hour * 60 + minute
        
        # If there are duplicate time points, the minimum difference is 0
        if len(timePoints) != len(set(timePoints)):
            return 0 
        
        # Convert all time points to minutes and sort them
        convertedList = sorted(map(convertTime, timePoints))
        
        # Initialize the minimum difference to a large number
        minDifference = float('inf')
        
        # Compare adjacent times and calculate the minimum difference
        for i in range(1, len(convertedList)):
            minDifference = min(minDifference, convertedList[i] - convertedList[i - 1])
        
        # Compare the first and last time points to account for the circular nature of the clock
        minDifference = min(minDifference, 1440 + convertedList[0] - convertedList[-1])
        
        return minDifference
