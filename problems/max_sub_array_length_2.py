from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        sum_indices = {0: -1}  # To handle the case where subarray starts from index 0
        max_length = 0

        print("Initial State:")
        print(f"nums = {nums}, k = {k}")
        print(f"prefix_sum = {prefix_sum}")
        print(f"sum_indices = {sum_indices}")
        print(f"max_length = {max_length}")
        print("-" * 50)

        for i, num in enumerate(nums):
            prefix_sum += num
            print(f"After adding nums[{i}] = {num}:")
            print(f"prefix_sum = {prefix_sum}")

            # Check if prefix_sum - k exists in the map
            if prefix_sum - k in sum_indices:
                current_length = i - sum_indices[prefix_sum - k]
                max_length = max(max_length, current_length)
                print(f"Found prefix_sum - k = {prefix_sum - k} in sum_indices.")
                print(f"Previous index = {sum_indices[prefix_sum - k]}")
                print(f"Current subarray length = {current_length}")
                print(f"Updated max_length = {max_length}")
            else:
                print(f"prefix_sum - k = {prefix_sum - k} not found in sum_indices.")

            # Store the first occurrence of this prefix_sum
            if prefix_sum not in sum_indices:
                sum_indices[prefix_sum] = i
                print(f"Stored prefix_sum {prefix_sum} at index {i} in sum_indices.")
            else:
                print(f"prefix_sum {prefix_sum} already exists in sum_indices at index {sum_indices[prefix_sum]}.")

            print(f"Current sum_indices: {sum_indices}")
            print("-" * 50)

        print(f"Final max_length: {max_length}")
        return max_length

nums = [1, -1, 5, -2, 3]
k = 3
max_length = Solution.maxSubArrayLen(None, nums, k)
