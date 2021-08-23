# Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

# Return the indices of the two numbers(1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Input: numbers = [2, 7, 11, 15], target = 9
# Output: [1, 2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

# Input: numbers = [-1, 0], target = -1
# Output: [1, 2]

# Input: numbers = [2, 3, 4], target = 6
# Output: [1, 3]

from typing import List


class Solution:
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(numbers):
            second = target - num
            if second in seen:
                return([seen[second]+1, index+1])
            seen[num] = index
        return []


solution = Solution()
nums = [2, 7, 11, 15]
target = 13
indexs = solution.two_sum(nums, target)
print(indexs)
