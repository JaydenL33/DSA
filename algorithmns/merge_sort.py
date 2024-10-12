
from typing import List


def sortArray(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    def merge(left_array, right_array):
        result = []
        i, j = 0, 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                result.append(left_array[i])
                i += 1
            else:
                result.append(right_array[j])
                j += 1
        result.extend(left_array[i:])
        result.extend(right_array[j:])
        return result

    # initalising at 0
    # Middle point with int division
    m = len(nums) // 2
    left_sorted = sortArray(nums[:m])
    right_sorted = sortArray(nums[m:])
    return merge(left_sorted, right_sorted)

nums = [5,2,3,1,16]
print(sortArray(nums))