# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example 1   given Input => nums = [2,7,11,15], target = 9      output => [0,1]
# Example 2   given Input => nums = [3,3], target = 6            output => [0,1]
#  Example 3  given Input => nums = [3,2,4], target = 6          output => [1,2]

from typing import List


# BruteForce Solution : Takes more time but less space
class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            first_index = nums.index(num)
            if (target-num) in nums[first_index+1:]:
                return([first_index, nums.index(target-num, first_index+1,)])


#  One-Pass Hash Table solution : Takes less time but more space
# class Solution:
#     def two_sum(self, nums, target):
#         seen = {}
#         for index, num in enumerate(nums):
#             remaining = target - num
#             if remaining in seen:
#                 return [seen[remaining], index]
#             seen[num] = index
#         return []


solution = Solution()
nums = [3, 3]
target = 6
indexs = solution.two_sum(nums, target)
print(indexs)
