from typing import List

# Function to return the sorted squares of the integers in the input list
def sortedSquares(nums: List[int]) -> List[int]:
    result = []
    l = 0
    r = len(nums) - 1
    while l <= r:
        l_sqr = nums[l] * nums[l]
        r_sqr = nums[r] * nums[r]
        if l_sqr > r_sqr:
            result.append(l_sqr)
            l += 1
        else:
            result.append(r_sqr)
            r -= 1
    return result[::-1]
    

# Test cases to validate the function
if __name__ == "__main__":
    # Test case 1: Mix of negative and positive numbers
    nums1 = [-4, -1, 0, 3, 10]
    assert sortedSquares(nums1) == [0, 1, 9, 16, 100], f"Test case 1 failed: {sortedSquares(nums1)}"
    
    # Test case 2: All negative numbers
    nums2 = [-7, -3, -1]
    assert sortedSquares(nums2) == [1, 9, 49], f"Test case 2 failed: {sortedSquares(nums2)}"
    
    # Test case 3: All positive numbers
    nums3 = [2, 3, 5]
    assert sortedSquares(nums3) == [4, 9, 25], f"Test case 3 failed: {sortedSquares(nums3)}"
    
    # Test case 4: Single element
    nums4 = [-2]
    assert sortedSquares(nums4) == [4], f"Test case 4 failed: {sortedSquares(nums4)}"
    
    # Test case 5: Empty list
    nums5 = []
    assert sortedSquares(nums5) == [], f"Test case 5 failed: {sortedSquares(nums5)}"
    
    print("All test cases passed!")