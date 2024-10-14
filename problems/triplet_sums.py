from typing import List


def n3divisibleTripletCount(nums: List[int], d: int) -> int:
    if len(nums) < 3:
        return 0
    results = []
    i, j, k = 0, 1, 2
    while i < len(nums) - 2:
        j = i + 1  # Reset j to be greater than i
        while j < len(nums) - 1:
            k = j + 1  # Reset k to be greater than j
            while k < len(nums):
                if (nums[i] + nums[j] + nums[k]) % d == 0:
                    results.append([i, j, k])
                k += 1
            j += 1
        i += 1
    return len(results)  # Returning the count of triplets instead of the list itself


def divisibleTripletCount(nums: List[int], d: int) -> int:
    if len(nums) < 3:
        return 0
    storage = []
    for num in nums:
        storage.append(num % d)
        print(storage)
    

nums = [3,3,4,7,8]
print(divisibleTripletCount(nums, 5)) # Expected: 3
nums = [3,3,3,3]
print(divisibleTripletCount(nums, 3)) # Expected: 4
print(divisibleTripletCount(nums, 6)) # Expected: 0

