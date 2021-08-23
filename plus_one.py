# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Input: digits = [1, 2, 3]
# Output: [1, 2, 4]
# Explanation: The array represents the integer 123.

# Input: digits = [4, 3, 2, 1]
# Output: [4, 3, 2, 2]
# Explanation: The array represents the integer 4321.
from typing import List


class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:
        digits = int(''.join(map(str, digits)))
        digits += 1
        return list(map(int, list(str(digits))))


solution = Solution()
nums = solution.plus_one([4, 3, 2, 1, 1])
print(nums)
