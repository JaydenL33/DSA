from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        resultList = []
        for i in range(len(nums)):
            if nums[i] not in resultList:
                resultList.append(nums[i])
            else:
                resultList.remove(nums[i])
        return resultList[0]
            
            