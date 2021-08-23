# Given an integer array nums sorted in non-decreasing order, remove the duplicates in -place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in -place with O(1) extra memory.

import time
# Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
from typing import List

# solution what did foolishly but it was not needed to be this complicated
# class Solution:
#     def remove_duplicates(self, nums: List[int]) -> int:
#         if(len(nums) == 0):
#             return (0)
#         for index in range(len(nums)):
#             if nums[-index-1] in nums[:-index-1]:
#                 nums.pop(-index-1)
#                 nums.append('_')
#         if('_' in nums):
#             return (nums.index('_'))
#         else:
#             return (len(nums))


class Solution:
    def remove_duplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        return len(nums)


solution = Solution()
t = time.time()
nums = [1, 1, 1, 2, 3, 3, 4]*1000
k = solution.remove_duplicates(nums)
print(time.time()-t)
